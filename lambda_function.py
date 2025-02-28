import json
import base64
from license_plate_reader import LicensePlateReader, NotLicensePlateFoundException, FormattingImageException

def lambda_handler(event, context):
    try:
        license_plate_reader = LicensePlateReader()
        body = json.loads(event['body'])
        image_bytes = base64.b64decode(body['imageBase64'])
        min_confidence = body['minConfidence']
        license_plate = license_plate_reader.get_license_plate(image_bytes, min_confidence)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "licensePlate": license_plate
            })
        }
    except NotLicensePlateFoundException as e:
        return {
            "statusCode": 404,
            "body": json.dumps({
                "error": str(e)
            })
        }
    except (FormattingImageException, Exception) as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
