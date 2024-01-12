import os
import cv2 as cv
import pyexiv2


def crop_images(images, size, debug=False, show=False, save=False):
    cropped_images = []
    for i,image in enumerate(images):
        print(f"Processing image {i+1}/{len(images)}")
        cropped_image = crop_image(image, size, debug, show, save)
        cropped_images.append(cropped_image)
    return cropped_images

def crop_image(image_path, size, debug=False, show=False, save=False):
    img = cv.imread(image_path)
    # Get image size
    height, width = img.shape[:2]
    # Compute crop size
    crop_height = min(height, size[0])
    crop_width = min(width, size[1])
    # Compute crop offset
    offset_x = (width - crop_width) // 2
    offset_y = (height - crop_height) // 2
    # Crop image
    cropped_image = img[offset_y:offset_y+crop_height, offset_x:offset_x+crop_width]
    # Show debug images
    if debug:
        cv.imshow("Original", cv.resize(img, (1000, 600)))
        cv.imshow("Cropped", cv.resize(cropped_image, (1000, 600)))
        cv.waitKey(0)
    # Show cropped image
    if show:
        cv.imshow("Cropped", cv.resize(cropped_image, (1000, 600)))
        cv.waitKey(0)
    # Save cropped image
    if save:
        out_path = f"{SOURCE_PATH}/cropped/{OBJECT_NAME}_" + image_path[-7:]
        cv.imwrite(out_path, cropped_image)

        # Copy metadata from original image to cropped image
        in_metadata = pyexiv2.Image(image_path)
        out_metadata = pyexiv2.Image(out_path)
        out_metadata.modify_exif(in_metadata.read_exif())

    return cropped_image

# Usage
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Crop images")
    parser.add_argument("source", type=str, help="Path to source directory containing images to crop")
    args = parser.parse_args()

    # Get source path
    SOURCE_PATH = args.source

    # Get list of images
    files = []
    img_shape = None
    for file in os.listdir(SOURCE_PATH):
        if file.endswith("merged.jpg"):
            img_shape = cv.imread(f"{SOURCE_PATH}/{file}").shape[:2]
            print("Image shape:", img_shape)
        elif file.endswith(".jpg"):
            files.append(f"{SOURCE_PATH}/{file}")
    print("Number of images:", len(files))
    
    if len(files) > 0:
        if img_shape is None:
            raise Exception(f"Merged image not found. Check if it is in the source directory, and that the correct path is provided.")
        
        # Create output directory
        if not os.path.exists(f"{SOURCE_PATH}/cropped/"):
            os.makedirs(f"{SOURCE_PATH}/cropped/")

        # Get object name
        OBJECT_NAME = "_".join(files[0].split("/")[-1].split("_")[:-1])
        print("Object name:", OBJECT_NAME)

        # Crop images
        cropped_images = crop_images(files, img_shape, debug=False, show=False, save=True)