from license_plate_reader import LicensePlateReader
import base64

def lambda_handler(event, context):
    license_plate_reader = LicensePlateReader()
    image_bytes = base64.b64decode(event['imageBase64'])
    min_confidence = event['minConfidence']
    license_plate = license_plate_reader.get_license_plate(image_bytes, min_confidence)

    return {
        "statusCode": 200,
        "body": {
            "licensePlate": license_plate
        }
    }
