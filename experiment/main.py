import cv2
import numpy as np
import requests
from PIL import Image

def rgb_to_hex(rgb):
    """Converts RGB values (tuple or list of 3 integers) to a hex string."""
    if len(rgb) != 3:
        raise ValueError("Input must be a tuple or list of 3 integers (RGB values).")
    return '#%02x%02x%02x' % tuple(rgb)

# Unduh gambar (jika perlu) dan baca gambar
url = 'https://static.notpx.app/templates/6488960520.png'
response = requests.get(url, stream=True)
img_pil = Image.open(response.raw)
img = np.array(img_pil)

# Tentukan koordinat pixel yang diinginkan
row = 19
col = 20

try:
  # Akses pixel dengan koordinat yang ditentukan
  pixel_value = img[row, col]
  pixel_value = [pixel_value[0], pixel_value[1], pixel_value[2]]
  if len(pixel_value) == 3:  # Check if pixel value is RGB
      hex_color = rgb_to_hex(pixel_value).upper()
      print(f"Pixel at ({row}, {col}): {hex_color}")
  else:
      print(f"Pixel at ({row}, {col}) is not RGB: {pixel_value}")
except IndexError as e:
  print(f"Error: Invalid coordinates ({row}, {col}). Image dimensions are {img.shape[0]}x{img.shape[1]}.")