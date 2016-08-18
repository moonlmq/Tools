import cv2
#imread return a BGR color format image
image = cv2.imread('pika.jpg')
cv2.imwrite('pika.png',image)
#imread can specify mode by
# IMREAD_ANYCOLOR = 4
 # IMREAD_ANYDEPTH = 2
 # IMREAD_COLOR = 1
 # IMREAD_GRAYSCALE = 0
 # IMREAD_LOAD_GDAL = 8
 # IMREAD_REDUCED_COLOR_2 = 17
 # IMREAD_REDUCED_COLOR_4 = 33
 # IMREAD_REDUCED_COLOR_8 = 65
 # IMREAD_REDUCED_GRAYSCALE_2 = 16
 # IMREAD_REDUCED_GRAYSCALE_4 = 32
 # IMREAD_REDUCED_GRAYSCALE_8 = 64
 # IMREAD_UNCHANGED = -1
grayImage = cv2.imread('pika.png',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('graypika.png',grayImage)