import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import os

folder_path = 'noisy\chemical'
clean_image_path = 'cleaned_images\chemical'

imgfp = 'noisy\chemical\inchi1.png'


#============================================== Analysis of different methods ==============================================

def analyse_techniques(img1):
    # Applying Gaussian Blur to smooth out the noise
    gaussian_blur1 = cv2.GaussianBlur(img1, (5, 5), 0)

    # Applying Median Blur to remove salt and pepper noise
    median_blur1 = cv2.medianBlur(img1, 3)

    # Applying Bilateral Filtering to reduce noise while keeping edges sharp
    bilateral_filter1 = cv2.bilateralFilter(img1, 9, 75, 75)

    thresholded_original1 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    thresholded_bilateral1 = cv2.adaptiveThreshold(bilateral_filter1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Display the results
    plt.figure(figsize=(14,7))

    plt.subplot(231), plt.imshow(img1, cmap='gray'), plt.title('Original')
    plt.subplot(232), plt.imshow(gaussian_blur1, cmap='gray'), plt.title('Gaussian Blur')
    plt.subplot(233), plt.imshow(median_blur1, cmap='gray'), plt.title('Median Blur')
    plt.subplot(234), plt.imshow(bilateral_filter1, cmap='gray'), plt.title('Bilateral Filter - Image 1')
    plt.subplot(235), plt.imshow(thresholded_original1, cmap='gray'), plt.title('Thresholded Original - Image 1')
    plt.subplot(236), plt.imshow(thresholded_bilateral1, cmap='gray'), plt.title('Thresholded Bilateral - Image 1')
    
    plt.tight_layout()
    plt.show()


def clean_image(img):
#     img = cv2.dilate(img, np.ones((1,1), np.uint8), iterations=1)
    # Bilateral filter to preserve edges while reducing noise

    bilateral = cv2.bilateralFilter(img, 10, 100, 100)
    

    # Morphological opening to remove small noise

    kernel_vertical = np.array([[0, 1, 0],
                                [0, 1, 0],
                                [0, 1, 0]], dtype=np.uint8)

    kernel_horizontal = np.array([[0, 0, 0],
                                  [1, 1, 1],
                                  [0, 0, 0]], dtype=np.uint8)

    kernel_diagonal_1 = np.array([[1, 0, 0],
                                  [0, 1, 0],
                                  [0, 0, 1]], dtype=np.uint8)

    kernel_diagonal_2 = np.array([[0, 0, 1],
                                  [0, 1, 0],
                                  [1, 0, 0]], dtype=np.uint8)

    # Apply morphological operations separately
    vertical_lines = cv2.morphologyEx(bilateral, cv2.MORPH_OPEN, kernel_vertical)
    horizontal_lines = cv2.morphologyEx(bilateral, cv2.MORPH_OPEN, kernel_horizontal)
    diagonal_lines_1 = cv2.morphologyEx(bilateral, cv2.MORPH_OPEN, kernel_diagonal_1)
    diagonal_lines_2 = cv2.morphologyEx(bilateral, cv2.MORPH_OPEN, kernel_diagonal_2)

    opening = np.maximum.reduce([vertical_lines, horizontal_lines, diagonal_lines_1, diagonal_lines_2])

    

    # Morphological closing to fill gaps

    vertical_lines =   cv2.morphologyEx(opening,   cv2.MORPH_CLOSE, kernel_vertical)
    horizontal_lines = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel_horizontal)
    diagonal_lines_1 = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel_diagonal_1)
    diagonal_lines_2 = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel_diagonal_2)
    closing = np.minimum.reduce([vertical_lines, horizontal_lines, diagonal_lines_1, diagonal_lines_2])
 

    return closing

if os.path.exists(imgfp):
    img = cv2.imread(imgfp, cv2.IMREAD_GRAYSCALE)
    analyse_techniques(img)


if len(sys.argv) > 1:
    folder_path = sys.argv[1]

for filename in os.listdir(folder_path):
    img = cv2.imread(os.path.join(folder_path, filename), cv2.IMREAD_GRAYSCALE)
    img_clean = clean_image(img)
    cv2.imwrite(os.path.join(clean_image_path, filename), img_clean)
    print(f"{filename} processed.")