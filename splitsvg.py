import xml.etree.ElementTree as ET
import os
import copy

def split_svg_into_tiles(svg_path, output_directory, tile_width, tile_height):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    namespaces = {'svg': 'http://www.w3.org/2000/svg'}
    tree = ET.parse(svg_path)
    root = tree.getroot()
    rects = root.findall('.//svg:rect', namespaces)

    max_width = max(int(rect.get('x')) + int(rect.get('width')) for rect in rects)
    max_height = max(int(rect.get('y')) + int(rect.get('height')) for rect in rects)

    num_tiles_x = max_width // tile_width + (1 if max_width % tile_width > 0 else 0)
    num_tiles_y = max_height // tile_height + (1 if max_height % tile_height > 0 else 0)

    for i in range(num_tiles_y):
        for j in range(num_tiles_x):
            tile_svg = ET.Element('svg', width=str(tile_width), height=str(tile_height), xmlns="http://www.w3.org/2000/svg")

            for rect in rects:
                x, y = int(rect.get('x')), int(rect.get('y'))
                if j * tile_width <= x < (j + 1) * tile_width and i * tile_height <= y < (i + 1) * tile_height:
                    # Clone the rect to avoid modifying the original
                    new_rect = copy.deepcopy(rect)
                    # Adjust the rect's position relative to the tile
                    new_rect.set('x', str(x - j * tile_width))
                    new_rect.set('y', str(y - i * tile_height))
                    tile_svg.append(new_rect)

            # Serialize and save the SVG tile
            tile_tree = ET.ElementTree(tile_svg)
            tile_path = os.path.join(output_directory, f'tile_{i}{j}.svg')
            tile_tree.write(tile_path)
    
    print(f"Tiles have been saved to {output_directory}")


svg_path = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/NB_after500_2D.svg'
output_directory = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/Splitimagessvg'
tile_width, tile_height = 256, 256  # Set your desired tile width and height

split_svg_into_tiles(svg_path, output_directory, tile_width, tile_height)
