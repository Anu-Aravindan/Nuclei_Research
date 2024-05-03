from PIL import Image

# Load the two images
image1_path = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/Undeformed_New.png'
image2_path = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/Tracking/Undeformed_Prediction.png'

image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

# Ensure the images have the same size
# image2 = image2.resize(image1.size, Image.ANTIALIAS)

# Make the image2 more transparent to see through it
image2.putalpha(128)  # Adjust the alpha channel; 0 is fully transparent, 255 is fully opaque

# Overlay image2 on top of image1
combined = Image.alpha_composite(image1.convert('RGBA'), image2.convert('RGBA'))

# Save the result
combined_path = '/Users/anuraagaravindan/Desktop/image_Processing-nonGit/overlay_Undeformed.png'
combined.save(combined_path)

print(f"Combined image saved as {combined_path}")
