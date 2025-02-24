import base64
from license_plate_reader import LicensePlateReader

def main():
    license_plate_reader = LicensePlateReader()
    image = base64.b64decode(getBase64())
    min_confidence = 90
    license_plate = license_plate_reader.get_license_plate(image, min_confidence)

    print(license_plate)


def getBase64() -> str:
    return 'base64StringHere'

if __name__ == "__main__":
    main()
