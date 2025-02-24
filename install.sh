#!/bin/bash
# Clean up previous builds
rm -rf package deployment-package.zip
mkdir package

# Install dependencies into the 'package' folder
pip install -r requirements.txt --target ./package

# Zip the dependencies
cd package
zip -r ../deployment-package.zip .
cd ..

# Add your Python files to the deployment package
zip -g deployment-package.zip lambda_function.py image_utils.py license_plate_reader.py
