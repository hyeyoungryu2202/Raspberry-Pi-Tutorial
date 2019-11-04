# Import the required libraries
import cv2
import numpy as np
import pytesseract
from PIL import Image
from pytesseract import image_to_string

# Path of working folder on Disk
# Instead of the path written below, write the path for your file
src_path = "/Users/angieryu2202/Desktop/RaspberryPiTutorials/businesscardimg/02.jpg"

# Define function to get the strings (texts and digits) from the image
def get_string(src_path):
    # Read image with opencv
    img = cv2.imread(src_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "removed_noise.png"))

    return result

print('--- Start recognize text from image ---')
# Print the texts and digits read from the image
print(get_string(src_path))

print("------ Done -------")
