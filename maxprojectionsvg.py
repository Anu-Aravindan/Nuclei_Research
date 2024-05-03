import imageio
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import svgwrite

undeformed = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/NB_after500.tif'
save_path = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/NB_after500_2D.svg' 

def calculate_maximum_projection_with_roi(tiff_file_path, save_path):
    tiff_stack = imageio.volread(tiff_file_path)
    
    if len(tiff_stack.shape) != 3:
        print("The provided TIFF file does not seem to be a 3D stack.")
        return
    
    # Convert the RGB or RGBA images to grayscale
    tiff_stack_gray = [np.array(Image.fromarray(slice_rgb).convert('L')) for slice_rgb in tiff_stack]
    max_projection = np.max(tiff_stack_gray, axis=0)

    # Create an SVG drawing with explicit dimensions matching the image size
    dwg = svgwrite.Drawing(save_path, size=(max_projection.shape[1], max_projection.shape[0]), profile='tiny')

    # Optional: Set the pixel size for each square in the SVG
    pixel_size = 1  # Size of the square representing a pixel

    # Convert the numpy array to squares in the SVG
    for y in range(max_projection.shape[0]):
        for x in range(max_projection.shape[1]):
            intensity = max_projection[y, x]
            color = svgwrite.rgb(intensity, intensity, intensity, mode='RGB')
            dwg.add(dwg.rect(insert=(x * pixel_size, y * pixel_size), size=(pixel_size, pixel_size), fill=color))

    dwg.save()
    print(f"Maximum intensity projection saved as SVG: {save_path}")

calculate_maximum_projection_with_roi(undeformed, save_path)

