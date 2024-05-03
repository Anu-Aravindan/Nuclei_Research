import os
from PIL import Image
import numpy as np

# Path to the directory containing the images
image_width = 2304
image_height = 512
tile_size = 128

mod = int(image_width/tile_size)

folder_path = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/Undeformed_Prediction_Tiles'
image_files = sorted([os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.png')])


full_image = np.zeros((image_height, image_width, 3), dtype=np.uint8)

for i, file_path in enumerate(image_files):
    img = Image.open(file_path)
    img_array = np.array(img)

    if img_array.shape[2] == 4:
        img_array = img_array[:, :, :3]

    row = i // mod * tile_size
    col = i % mod * tile_size

    full_image[row:row+tile_size, col:col+tile_size] = img_array

# Convert the full image back to a PIL image
final_image = Image.fromarray(full_image)


# Save the rotated image
save_path = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/Tracking/Undeformed_Prediction.png'
final_image.save(save_path)
final_image.show()
