from PIL import Image, ImageOps

img1_path = "/Users/anuraagaravindan/Desktop/image_Processing-nonGit/Tracking/1_Undeformed_Prediction_new.png"
img2_path = "/Users/anuraagaravindan/Desktop/image_Processing-nonGit/Tracking/2_Deformed_Prediction_new.png"
img1 = Image.open(img1_path)
img2 = Image.open(img2_path)

def rescale_image(img):
    width, height = img.size
    new_size = (width * 3, height * 3)
    return img.resize(new_size, resample=Image.NEAREST)

rescaled_img1 = rescale_image(img1)
rescaled_img2 = rescale_image(img2)

rescaled_img1.save("/Users/anuraagaravindan/Desktop/image_Processing-nonGit/Tracking_Rescaled/1_Undeformed_Prediction_Rescale.png")
rescaled_img2.save("/Users/anuraagaravindan/Desktop/image_Processing-nonGit/Tracking_Rescaled/2_Deformed_Prediction_Rescale.png")
