import cv2
import numpy
import utils	

def recolorRC(src,dst):
	"""Simulate conversion from BGR to RC(red,cyan).
	The source and destination images must both be in BGR format.
	Blues and greens are replaced with cyans.
	Pseudocde:
	dst.b = dst.g = 0.5 *(src.b+src.g)
	dst.r = src.r
	"""

	#extact source image's channels as one-dimensional arrays
	b,g,r = cv2.split(src)
	#replace the B channel's values with an average of B and G
	cv2.addWeighted(b,0.5,g,0.5,0,b)
	#replace the values in destination image with the modified channels
	#use b twice as an argument because the destination's B and G channels
	#should be equal
	cv2.merge((b,b,r),dst)


def recolorRGV(src,dst):
	"""Simulate conversion from BGR to RGV(red,green,value)
	The source and destination images must both be in BGR format.
	Blues are desaturated.
	Pseudocode:
	dst.b = min(src.b,src.g,src.r)
	dst.g = src.g
	dst.r = src.r
	"""

	b,g,r = cv2.split(src)
	#min() compute the per-element minimums of first two arguments
	#and writes them to the third argument
	cv2.min(b,g,b)
	cv2.min(b,r,b)
	cv2.merge((b,g,r),dst)

def recolorCMV(src,dst):
	"""Simulate conversion from BGR to CMV(cyan,magenta,value)
	The source and destination images must both be in BGR format.
	Yellows are desaturated.
	Pseudocode:
	dst.b = max(src.b,src.g,src.r)
	dst.g = src.g
	dst.r = src.r
	"""

	b,g,r = cv2.split(src)
	#max() compute the per-element maximums of first two arguments
	#and writes them to the third argument
	cv2.max(b,g,b)
	cv2.max(b,r,b)
	cv2.merge((b,g,r),dst)