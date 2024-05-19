import pydicom
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import os

def load_dicom_folder(folder_path):
    # Load all DICOM files from the specified folder and sort them by SliceLocation
    dicom_files = [pydicom.dcmread(os.path.join(folder_path, f)) for f in os.listdir(folder_path) if f.endswith('.dcm')]
    dicom_files.sort(key=lambda x: float(x.SliceLocation))
    return dicom_files

def stack_dicom_images(dicom_files):
    # Assuming all DICOM images have the same dimensions and number of channels
    num_images = len(dicom_files)
    image_shape = dicom_files[0].pixel_array.shape
    stacked_volume = np.zeros((num_images, *image_shape), dtype=np.float32)

    # Stack images into a 3D numpy array
    for i, dicom_file in enumerate(dicom_files):
        stacked_volume[i, :, :] = dicom_file.pixel_array
    
    return stacked_volume

def visualize_with_slider(stacked_volume):
    # Initial slice index
    initial_slice = len(stacked_volume) // 2

    # Create the figure and axis
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.25)
    
    # Display the initial slice
    img_display = ax.imshow(stacked_volume[initial_slice, :, :], cmap='gray')
    ax.set_title(f'Slice {initial_slice}')

    # Create the slider
    ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
    slice_slider = Slider(ax_slider, 'Slice', 0, len(stacked_volume) - 1, valinit=initial_slice, valfmt='%0.0f')

    # Update function for the slider
    def update(val):
        slice_idx = int(slice_slider.val)
        img_display.set_data(stacked_volume[slice_idx, :, :])
        ax.set_title(f'Slice {slice_idx}')
        fig.canvas.draw_idle()

    # Connect the update function to the slider
    slice_slider.on_changed(update)

    # Show the plot
    plt.show()

## Main part
folder_path = 'dicom_imgs_46'

dicom_files = load_dicom_folder(folder_path)
stacked_volume = stack_dicom_images(dicom_files)
visualize_with_slider(stacked_volume)
