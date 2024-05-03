import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

lowerbound = 20
upperbound = 60

def apply_threshold(input_dir, output_dir, threshold=120):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            file_path = os.path.join(input_dir, filename)
            image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
            
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, binary_image)

def clean_images(input_dir, output_dir, min_size, max_size, kernel_size=2):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            file_path = os.path.join(input_dir, filename)
            image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            convolved_image = cv2.filter2D(image, -1, np.ones((kernel_size, kernel_size), np.float32) / (kernel_size**2))

            nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(convolved_image, connectivity=8)
            sizes = stats[1:, -1]  
            nb_components = nb_components - 1

            cleaned_image = np.zeros(output.shape, np.uint8)
            for i in range(0, nb_components):
                if min_size <= sizes[i] <= max_size:
                    cleaned_image[output == i + 1] = 255
            
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, cleaned_image)


def create_visualization(original_dir, thresholded_dir, cleaned_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(original_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            original_path = os.path.join(original_dir, filename)
            thresholded_path = os.path.join(thresholded_dir, filename)
            cleaned_path = os.path.join(cleaned_dir, filename)

            original_image = cv2.imread(original_path, cv2.IMREAD_GRAYSCALE)
            thresholded_image = cv2.imread(thresholded_path, cv2.IMREAD_GRAYSCALE)
            cleaned_image = cv2.imread(cleaned_path, cv2.IMREAD_GRAYSCALE)

            fig, axes = plt.subplots(1, 3, figsize=(12, 4))
            titles = ['Original', 'Binary Threshold', 'Convolution Final']
            
            image_spacing = 0.05
            font_size = 10

            for ax, img, title in zip(axes, [original_image, thresholded_image, cleaned_image], titles):
                ax.imshow(img, cmap='gray')
                ax.set_title(title, fontsize=font_size)
                ax.axis('off')

            plt.subplots_adjust(wspace=image_spacing, hspace=0)

            visualization_path = os.path.join(output_dir, f"visualization_{filename}")
            plt.savefig(visualization_path, bbox_inches='tight', pad_inches=0.1)
            plt.close()


input_directory = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/SplitImages' 
output_directory1 = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/SplitImagesThreshold'
output_directory2 = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/SplitImagesConvolution'
viz_directory = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/visualizations'

# input1 = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/drive-download-20240410T205611Z-001'
# mask_filter = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/MaskBinary'
 
# Uncomment the function you want to use
apply_threshold(input_directory, output_directory1, 128)
clean_images(output_directory1, output_directory2, upperbound, lowerbound)
apply_threshold(output_directory2, output_directory2, 40)
create_visualization(input_directory, output_directory1, output_directory2, viz_directory)

# apply_threshold(input1, mask_filter, 40)
# apply_threshold(output_directory2, output_directory2, 40)

# clean_images(output_directory2, output_directory2, 2, 20)

