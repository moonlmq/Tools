import cv2
import numpy
import os

"""
An OpenCV image is a 2D or 3D array of type numpy.array. An 8-bit grayscale
image is a 2D array containing byte values. A 24-bit BGR image is a 3D array, also
containing byte values. We may access these values by using an expression like
image[0, 0] or image[0, 0, 0]. The first index is the pixel's y coordinate, or row,
0 being the top. The second index is the pixel's x coordinate, or column, 0 being the
leftmost. The third index (if applicable) represents a color channel.
"""

# Make an array of 120,000 random bytes.
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)
# Convert the array to make a 400x300 grayscale image
grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('RandomGray.png',grayImage)

# Convert the array to make a 400x100 color image.
bgrImage = flatNumpyArray.reshape(100,400,3)
cv2.imwrite('RandomColor.png',bgrImage)