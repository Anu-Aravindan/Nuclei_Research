import os
from PIL import Image, ImageDraw, ImageFont
import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# tiff_path = "/Users/anuraagaravindan/Desktop/image_Processing-nonGit/NB_after500.tif"
save_path_png = "/Users/anuraagaravindan/Desktop/image_Processing-nonGit/Undeformed_New.png"
output_dir = "/Users/anuraagaravindan/Desktop/image_Processing-nonGit/SplitImagesTest_Undeformed"

def calculate_maximum_projection(tiff_file_path, save_path_png):
    tiff_stack = imageio.volread(tiff_file_path)
    
    if len(tiff_stack.shape) != 3:
        print("The provided TIFF file does not seem to be a 3D stack.")
        return None
    
    tiff_stack_gray = [np.array(Image.fromarray(slice_rgb).convert('L')) for slice_rgb in tiff_stack]
    max_projection = np.max(tiff_stack_gray, axis=0)

    Image.fromarray(max_projection).save(save_path_png)
    print(max_projection.shape)
    print(f"Maximum projection image saved as: {save_path_png}")
    return save_path_png

def split_image_into_tiles_with_visualization(image_path, output_dir, tile_width=128, tile_height=128):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    original_image = Image.open(image_path).convert('L')
    original_width, original_height = original_image.size

    num_tiles_x = original_width // tile_width
    num_tiles_y = original_height // tile_height

    if original_width % tile_width != 0:
        num_tiles_x += 1
    if original_height % tile_height != 0:
        num_tiles_y += 1

    fig, ax = plt.subplots()
    ax.imshow(original_image, cmap='gray')
    ax.set_xticks(np.arange(0, original_width, tile_width))
    ax.set_yticks(np.arange(0, original_height, tile_height))
    ax.grid(which='both', color='r', linestyle='-', linewidth=2)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    count = 10

    for i in range(num_tiles_y):
        for j in range(num_tiles_x):
            left = j * tile_width
            upper = i * tile_height
            right = min(left + tile_width, original_width)
            bottom = min(upper + tile_height, original_height)

            tile = original_image.crop((left, upper, right, bottom))
            tile_path = os.path.join(output_dir, f"mask_{count}.png")
            count += 1
            tile.save(tile_path)

            text_x = left + tile_width - 50  
            text_y = upper + 10
            ax.add_patch(patches.Rectangle((text_x, text_y), 40, 20, fill=True, color='black', alpha=0.5))

            ax.text(text_x + 20, text_y + 10, f'{i*num_tiles_x+j+1}', color='white', weight='bold', fontsize=8, ha='center', va='center')

    plt.savefig(os.path.join(output_dir, "visualization.png"))
    plt.show()
    print(f"Total tiles created: {num_tiles_x * num_tiles_y}")


# Example usage
# calculate_maximum_projection(tiff_path, save_path_png)
split_image_into_tiles_with_visualization(save_path_png, output_dir)
