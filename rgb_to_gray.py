import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

img=mpimg.imread('test_image.webp')

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

gray=rgb2gray(img)

plt.imshow(gray, cmap=plt.get_cmap('gray'))
plt.show()