from PIL import Image
import numpy as np

def combine_images_max_intensity(image1_path, image2_path, output_path):
    image1 = Image.open(image1_path).convert('L')
    image2 = Image.open(image2_path).convert('L')
    image1_array = np.array(image1)
    image2_array = np.array(image2)

    max_image_array = np.maximum(image1_array, image2_array)

    max_image = Image.fromarray(max_image_array)

    max_image.save(output_path)

image1_path = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/task-1-annotation-33-by-1-tag-Nuclei-0.png'
image2_path = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/task-1-annotation-33-by-1-tag-Nuclei-1.png'
output_path = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/task-1-annotation-33-by-1-tag-Nuclei-0.png'

combine_images_max_intensity(image1_path, image2_path, output_path)


