import imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Function to split image into smaller tiles and resize 
def split_and_resize_image(image, tile_size=256):
    width, height = image.size
    tiles = []
    tile_positions = []  # Store positions of each tile
    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            # Define the region to crop
            box = (x, y, x + tile_size, y + tile_size)
            tile = image.crop(box)
            # Resize the tile
            tile = tile.resize((256, 256), Image.LANCZOS)
            tiles.append(tile)
            tile_positions.append(box)
    return tiles, tile_positions

import svgwrite

def calculate_maximum_projection_with_roi(tiff_file_path, tile_size=256):
    tiff_stack = imageio.volread(tiff_file_path)
    
    if len(tiff_stack.shape) != 3:
        print("The provided TIFF file does not seem to be a 3D stack.")
        return
    
    tiff_stack_gray = [np.array(Image.fromarray(slice_rgb).convert('L')) for slice_rgb in tiff_stack]
    max_projection = np.max(tiff_stack_gray, axis=0)
    
    # Convert to PIL Image
    max_projection_pil = Image.fromarray(max_projection)
    
    # Split and resize the image
    tiles, tile_positions = split_and_resize_image(max_projection_pil, tile_size)
    
    # Create SVG drawing
    dwg = svgwrite.Drawing('tiles.svg', profile='tiny')
    
    for i, (tile, pos) in enumerate(zip(tiles, tile_positions)):
        # Draw the tile on a temporary image
        temp_image = Image.new("RGB", (tile_size, tile_size))
        temp_image.paste(tile, (0, 0))
        
        # Save the temporary image as PNG
        png_filename = f"tile_{i}.png"
        temp_image.save(png_filename)
        
        # Add PNG image to the SVG drawing
        dwg.add(svgwrite.image.Image(png_filename, insert=(pos[0], pos[1])))
        
        # Add label
        label_position = (pos[0] + 5, pos[1] + 5)
        dwg.add(dwg.text(str(i), insert=label_position, font_size=20, fill="red"))
    
    # Save main SVG drawing
    dwg.save()

# Example usage:
undeformed = '/Users/joserosa/Desktop/Particle_Tracking/NB_after500.tif'
calculate_maximum_projection_with_roi(undeformed, tile_size=256)