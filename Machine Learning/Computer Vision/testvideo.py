import cv2

videoCapture = cv2.VideoCapture('Input.avi')
fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),\
	int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
"""
cv2.cv.CV_FOURCC('I','4','2','0'): This is an uncompressed YUV, 4:2:0
chroma subsampled. This encoding is widely compatible but produces large
files. The file extension should be avi.
cv2.cv.CV_FOURCC('P','I','M','1'): This is MPEG-1. The file extension
should be avi.
cv2.cv.CV_FOURCC('M','J','P','G'): This is motion-JPEG. The file
extension should be avi.
cv2.cv.CV_FOURCC('T','H','E','O'): This is Ogg-Vorbis. The file
extension should be ogv.
cv2.cv.CV_FOURCC('F','L','V','1'): This is Flash video. The file
extension should be flv.
"""
videoWriter = cv2.VideoWriter('Output.avi',cv2.cv.CV_FOURCC('I','4','2','0'),fps, size)

success, frame = videoCapture.read()
while success: #Loop until there are no more frames.
	videoWriter.write(frame)
	success,frame = videoCapture.read()