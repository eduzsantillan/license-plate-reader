# Car License Plate Reader

This project is a car license plate reader application. It decodes base64 images and uses a license plate reader to extract license plate information.

## Features

- Base64 image decoding
- License plate reading with a minimum confidence level
- Simple command-line interface

## Requirements

- Python 3.x
- `boto3` (see [requirements.txt](cci:7://file:///Users/eduzuniga/Development/car-app/requirements.txt:0:0-0:0) for dependencies)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd car-app
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using the following command:
```bash
python app.py
```

The application will decode a base64 image string and print the detected license plate.

## File Structure

- [app.py](cci:7://file:///Users/eduzuniga/Development/car-app/app.py:0:0-0:0): Main application script
- [license_plate_reader.py](cci:7://file:///Users/eduzuniga/Development/car-app/license_plate_reader.py:0:0-0:0): Contains the `LicensePlateReader` class for reading license plates
- [image_utils.py](cci:7://file:///Users/eduzuniga/Development/car-app/image_utils.py:0:0-0:0): Utility functions for image processing
- [requirements.txt](cci:7://file:///Users/eduzuniga/Development/car-app/requirements.txt:0:0-0:0): Python dependencies
- [install.sh](cci:7://file:///Users/eduzuniga/Development/car-app/install.sh:0:0-0:0): Shell script for installation
- [lambda_function.py](cci:7://file:///Users/eduzuniga/Development/car-app/lambda_function.py:0:0-0:0): AWS Lambda function handler

## Contributing

Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

## Contact

For more information, please contact [Your Name] at [Your Email].
