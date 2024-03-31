import os
import sys
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
import matplotlib.pyplot as plt
import cv2

image_filepath = "rsna/00046/FLAIR/Image-71.dcm"

if len(sys.argv) > 1:
    image_filepath = sys.argv[1]

dcm_data = pydicom.dcmread(image_filepath)

print(dcm_data)

plt.imshow(dcm_data.pixel_array, cmap='gray')
plt.show()