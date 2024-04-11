import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import os

folder_path = 'noisy/speckle'
clean_image_path = 'cleaned_images/speckle'

def remove_speckle(img):
    denoised_image1 = cv2.medianBlur(img, 5)
    wiener_denoised_image1 = cv2.fastNlMeansDenoising(img, None, 30, 7, 21)
    plt.figure(figsize=(15, 5))  # Width, Height in inches

    # Plot original 
    plt.subplot(1, 3, 1)  
    plt.imshow(img, cmap='gray')
    plt.title('Original')
    plt.axis('off')  

    # Plot image 2
    plt.subplot(1, 3, 2)  
    plt.imshow(denoised_image1, cmap='gray')
    plt.title('Median Blur')
    plt.axis('off')  

    # Plot image 3
    plt.subplot(1, 3, 3)  
    plt.imshow(wiener_denoised_image1, cmap='gray')
    plt.title('Wiener Denoised')
    plt.axis('off')  

    # Display the plot
    plt.show()

    return denoised_image1, wiener_denoised_image1


if len(sys.argv) > 1:
    folder_path = sys.argv[1]

for filename in os.listdir(folder_path):
    img = cv2.imread(os.path.join(folder_path, filename), cv2.IMREAD_GRAYSCALE)
    img_clean1, img_clean2 = remove_speckle(img)
    cv2.imwrite(os.path.join(clean_image_path, 'medianBlur_'+filename), img_clean1)
    cv2.imwrite(os.path.join(clean_image_path, 'WienerDenoised_'+filename), img_clean2)

    print(f"{filename} processed.")

