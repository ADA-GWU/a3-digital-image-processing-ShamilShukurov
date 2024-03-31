Assignment 3 by Shamil Shukurov

**chemical.py**

This python file contains source code for cleaning chemical element images.

Usage: ```python3 chemical.py <folder_path>``` or just ```python3 chemical.py```

```folder_path``` is path to the folder where noisy chemical element images are saved. If folder path is not specified, default folderpath is ```'noisy\chemical'```
Program cleans the noisy images in the specified path and saves them in the folder ```'cleaned_images\chemical'```

This file also contains analysis of different techniques. I have tested different approaches on the first image. Here are the results:

![image](https://github.com/ADA-GWU/a3-digital-image-processing-ShamilShukurov/assets/81254972/edbc82e4-0c23-49b8-84e3-3c85caf06e03)

As you may see GaussianBlur is worst and ThresholdedBilateral is best case among tested techniques. Later I continued trying different filters and found final sequence of filters:
```
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
```
Since chemical elements contains lines (vertical, horizontal, diagonal) I tried to apply opening and closing with line:
![inchi1](https://github.com/ADA-GWU/a3-digital-image-processing-ShamilShukurov/assets/81254972/5061bc5c-b84e-4658-877a-978533c15762)

**speckle.py**

This python file contains source code for cleaning images with speckle noise.

Usage: ```python3 chemical.py <folder_path>``` or just ```python3 chemical.py```

```folder_path``` is path to the folder where noisy chemical element images are saved. If folder path is not specified, default folderpath is ```'noisy\speckle'```
Program cleans the noisy images in the specified path with 2 different approaches and saves them in the folder ```'cleaned_images\speckle'```
![image](https://github.com/ADA-GWU/a3-digital-image-processing-ShamilShukurov/assets/81254972/7feaa2fb-bf7b-4acb-9bf0-1b200ae96fa2)

