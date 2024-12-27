#Install Python 3 latest version on your computer
#install the pyzbar extension using the cmd command ```pip install pyzbar```
from PIL import Image, ImageFile
from pyzbar.pyzbar import decode
import os

# Increase or remove image size limits to prevent DecompressionBombError
Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Merge all barcode images in the folder into a single image
def merge_barcodes_in_folder(folder_path, output_path, direction="horizontal"):
    # Get all image files in the folder
    supported_formats = (".png", ".jpg", ".jpeg", ".bmp")
    image_paths = [
        os.path.join(folder_path, filename)
        for filename in os.listdir(folder_path)
        if filename.lower().endswith(supported_formats)
    ]

    if not image_paths:
        print("No barcode images found in the folder.")
        return False

    # Load images
    images = []
    for img_path in image_paths:
        try:
            with Image.open(img_path) as img:
                images.append(img.copy())  # Copy to keep in memory
        except Exception as e:
            print(f"Error loading image {img_path}: {e}")

    if not images:
        print("No valid images to process.")
        return False

    print(f"Loaded {len(images)} images.")

    # Determine canvas size and merge
    if direction == "horizontal":
        total_width = sum(img.width for img in images)
        max_height = max(img.height for img in images)
        canvas = Image.new("RGB", (total_width, max_height), "white")
        x_offset = 0
        for img in images:
            y_center = (max_height - img.height) // 2  # Center vertically
            canvas.paste(img, (x_offset, y_center))
            x_offset += img.width
    else:
        total_height = sum(img.height for img in images)
        max_width = max(img.width for img in images)
        canvas = Image.new("RGB", (max_width, total_height), "white")
        y_offset = 0
        for img in images:
            x_center = (max_width - img.width) // 2  # Center horizontally
            canvas.paste(img, (x_center, y_offset))
            y_offset += img.height

    # Save merged image
    try:
        canvas.save(output_path)
        print(f"Merged image saved at {output_path}")
        return True
    except Exception as e:
        print(f"Error saving merged image: {e}")
        return False

# Read barcodes from an image
def read_barcodes(image_path):
    try:
        img = Image.open(image_path)

        decoded_objects = decode(img)
        if not decoded_objects:
            print("No barcodes found in the image.")
            return

        for obj in decoded_objects:
            raw_data = obj.data
            decoded_data = raw_data.decode('utf-8').strip() if raw_data else "No Data"
            
            # Skip if data is empty or whitespace-only
            if not decoded_data:
                continue

            print(f"Type: {obj.type}, Data: {decoded_data}")
            print(f"Raw Data: {raw_data}")
            print(f"Bounding Box: {obj.rect}")

    except Exception as e:
        print(f"Error reading barcodes from {image_path}: {e}")

if __name__ == "__main__":
    # Update this path to the folder containing your barcode images
    barcode_folder = r"C:\Users\biggi\Downloads\Barcode_World"
    output_merged_image = r"C:\Users\biggi\Downloads\merged_barcodes.png"

    # Merge all barcodes in the folder and read them
    if merge_barcodes_in_folder(barcode_folder, output_merged_image, direction="horizontal"):
        read_barcodes(output_merged_image)
      
