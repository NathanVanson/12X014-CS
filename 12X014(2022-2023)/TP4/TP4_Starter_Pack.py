from PIL import Image
import numpy as np

# Example of image to illustrate the RGB format :

# This is a 4x4 image. Each pixel is defined by three values in the RGB system :
# first one is Red, second one is Green, third one is Blue.
# for ex, pixels[2] gives the 3rd row (index starts from 0) of the image,
# pixels[3][1] gives the pixel from the fourth row and second column,
# i.e. (204, 82, 122) in this example.

pixels = [
   [[54, 54, 54], [232, 23, 93], [255, 0, 0], [168, 167, 167]],
   [[204, 82, 122], [54, 54, 54], [168, 167, 167], [232, 23, 93]],
   [[0, 224, 0], [168, 167, 167], [0, 0, 200], [204, 82, 122]],
   [[168, 167, 167], [204, 82, 122], [232, 23, 93], [54, 54, 54]]
]


# Open an image and change it to an array (then you can work on an array
# similarly as with a list). You need to do a copy for the array
# (if you don't, you may have problems with permissions to write on file)

image_A = Image.open("Aerith.png")
pixels_image = np.asarray(image_A).copy()

# Get the size of an image :

long_A, haut_A = image_A.size

# changes the first 20x20 pixels in the corner of the array by black pixels :

for i in range(20):
    for j in range(20):
        for color in range(3):
            pixels_image[i][j][color] = 0

# Convert an array as an image and saving an image.
# Use png (jpg use compression and thus will destroy hidden content):

aerith_corner = Image.fromarray(pixels_image)
aerith_corner.save("Aerith_Dark.png")

# Now, find the hidden content in these images, and decrypt that cipherimage !
