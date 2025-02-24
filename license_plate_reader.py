import boto3
from botocore.exceptions import BotoCoreError, ClientError
import base64
import os
from image_utils import ImageUtils

class LicensePlateReader:
    LICENSE_PLATE = "License Plate"
    AWS_REGION = os.environ.get('AWS_REGION')

    def __init__(self):
        self.rekognition_client = boto3.client('rekognition', region_name=self.AWS_REGION)

    def get_license_plate(self, image: bytes, min_confidence: float) -> str:
        detected_labels = self.get_labels(self.convert_to_aws_image_request(image))
        bounding_box = self.get_license_plate_bounding_box(detected_labels, min_confidence)

        try:
            cropped_image = ImageUtils.crop_image(image, bounding_box['Left'], bounding_box['Top'], bounding_box['Width'],
                                            bounding_box['Height'])
        except Exception as e:
            raise FormattingImageException(f"Error cropping image: {e}")

        img_base64 = base64.b64encode(cropped_image).decode('utf-8')
        img_request_to_extract_text = self.convert_to_aws_image_request(cropped_image)

        return self.extract_text_from(img_request_to_extract_text)

    def get_labels(self, image):
        try:
            response = self.rekognition_client.detect_labels(Image=image)
            return response
        except (BotoCoreError, ClientError) as error:
            raise Exception(f"Error detecting labels: {error}")

    def get_license_plate_bounding_box(self, response, min_confidence):
        for label in response['Labels']:
            if label['Name'] == self.LICENSE_PLATE and label['Confidence'] >= min_confidence:
                return label['Instances'][0]['BoundingBox']
        raise NotLicensePlateFoundException("License plate not found")

    def extract_text_from(self, image):
        try:
            response = self.rekognition_client.detect_text(Image=image)
            result = ''.join(
                text_detection['DetectedText']
                for text_detection in response['TextDetections']
                if text_detection['Confidence'] >= 50 and 'ParentId' not in text_detection
            )
            if not result:
                raise NotLicensePlateFoundException("License plate not found")
            return result
        except (BotoCoreError, ClientError) as error:
            raise Exception(f"Error detecting text: {error}")

    def convert_to_aws_image_request(self, image: bytes):
        return {'Bytes': image}

class FormattingImageException(Exception):
    pass


class NotLicensePlateFoundException(Exception):
    pass