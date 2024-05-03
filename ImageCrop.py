from skimage import io

image1 = io.imread('/path/to/first/image.png')
image2 = io.imread('/path/to/second/image.png')

x, y = 100, 100 # starting x,y coordinates
width, height = 200, 200  # cropping length

crop_image1 = image1[y:y+height, x:x+width]
crop_image2 = image2[y:y+height, x:x+width]

io.imsave('/path/to/save/cropped_image1.png', crop_image1)
io.imsave('/path/to/save/cropped_image2.png', crop_image2)
