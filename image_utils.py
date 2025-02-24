from PIL import Image
import io

class ImageUtils:
    PADDING_PERCENTAGE = 0.1  # 10% padding

    @staticmethod
    def crop_image(image_data, left, top, width, height) -> bytes:
        original_image = Image.open(io.BytesIO(image_data))

        img_width, img_height = original_image.size

        # Add padding to dimensions
        padding_x = width * ImageUtils.PADDING_PERCENTAGE
        padding_y = height * ImageUtils.PADDING_PERCENTAGE

        # Adjust coordinates and dimensions with padding
        adjusted_left = max(0, left - padding_x)
        adjusted_top = max(0, top - padding_y)
        adjusted_width = min(1 - adjusted_left, width + (2 * padding_x))
        adjusted_height = min(1 - adjusted_top, height + (2 * padding_y))

        # Convert float values (0-1) to actual pixels
        x = round(adjusted_left * img_width)
        y = round(adjusted_top * img_height)
        w = round(adjusted_width * img_width)
        h = round(adjusted_height * img_height)

        # Ensure values are within image bounds
        x = max(0, min(x, img_width - 1))
        y = max(0, min(y, img_height - 1))
        w = min(w, img_width - x)
        h = min(h, img_height - y)

        cropped_image = original_image.crop((x, y, x + w, y + h))

        with io.BytesIO() as output:
            cropped_image.save(output, format="JPEG")
            return output.getvalue()