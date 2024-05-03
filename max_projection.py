import imageio
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

undeformed = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/NB_after500.tif'
save_path_png = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/NB_after500_2D.png' 

def calculate_maximum_projection_with_roi(tiff_file_path, save_path):
    tiff_stack = imageio.volread(tiff_file_path)
    
    if len(tiff_stack.shape) != 3:
        print("The provided TIFF file does not seem to be a 3D stack.")
        return
    
    tiff_stack_gray = [np.array(Image.fromarray(slice_rgb).convert('L')) for slice_rgb in tiff_stack]
    max_projection = np.max(tiff_stack_gray, axis=0)
    print(np.max(max_projection))
    num_pixels = max_projection.shape[0] * max_projection.shape[1]
    print(f"Number of pixels in the maximum projection image: {num_pixels}")
    
    # Save the image as a high-resolution PNG
    fig, ax = plt.subplots(figsize=(max_projection.shape[1] / 100, max_projection.shape[0] / 100), dpi=300)  # Adjust figsize based on your image dimensions and desired DPI
    ax.imshow(max_projection, cmap='gray', aspect='equal')
    ax.axis('off')  # Hide axes
    plt.savefig(save_path, format='png', bbox_inches='tight', dpi=300)
    plt.close(fig)  # Close the plot to free up memory
    print(f"Maximum intensity projection saved as high-resolution PNG: {save_path}")

calculate_maximum_projection_with_roi(undeformed, save_path_png)

