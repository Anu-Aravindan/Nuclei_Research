from skimage import io, color
from scipy import ndimage as nd
from matplotlib import pyplot as plt
from PIL import Image
from skimage.filters import median, gaussian
from skimage.morphology import disk
from skimage.transform import rescale
from skimage import exposure
from skimage.filters import unsharp_mask


img = io.imread("/Users/anuraagaravindan/Desktop/image_Processing-nonGit/image_new.png")
gray_img = color.rgb2gray(img[..., :3]) 
median_img = median(gray_img, disk(1))

upscaled_img = rescale(median_img, 1, anti_aliasing=True)

sharpened_img = unsharp_mask(upscaled_img, radius=1, amount=1)

equalized_img = exposure.equalize_adapthist(sharpened_img)
gaussian_img = gaussian(equalized_img, sigma=1)
equalized_img = exposure.equalize_adapthist(gaussian_img)
plt.imsave('/Users/anuraagaravindan/Desktop/image_Processing-nonGit/image_new_guassian.png',equalized_img)

# fig, axes = plt.subplots(1, 3, figsize=(18, 6))
# ax = axes.ravel()

# ax[0].imshow(upscaled_img, cmap='gray')
# ax[0].axis('off')
# ax[0].set_title('Upscaled Image')

# ax[1].imshow(sharpened_img, cmap='gray')
# ax[1].axis('off')
# ax[1].set_title('Sharpened Image')

# ax[2].imshow(equalized_img, cmap='gray')
# ax[2].axis('off')
# ax[2].set_title('Contrast Enhanced Image')

# plt.show()

