import os
from PIL import Image
import numpy as np

# Path to the directory containing the images
folder_path = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/Reconstruction_Tiles_OG'
image_files = sorted([os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.png')])

full_image = np.zeros((256, 768), dtype=np.uint8)

for i, file_path in enumerate(image_files):
    img = Image.open(file_path)
    img_array = np.array(img)

    row = i // 6 * 128 
    col = i % 6 * 128

    full_image[row:row+128, col:col+128] = img_array

# Convert the full image back to a PIL image
final_image = Image.fromarray(full_image)

# Save the final image
final_image.save('/Users/anuraagaravindan/Desktop/image_Processing-nonGit/Reconstructed_Tiles_OG.png')
final_image.show()