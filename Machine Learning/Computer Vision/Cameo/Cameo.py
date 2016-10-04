import cv2
import filters
from manage import WindowManager, CaptureManager
import rects
from trackers import FaceTracker

class Cameo(object):
	def __init__(self):
		self._windowManager = WindowManager('Cameo',self.onKeypress)
		self._captureManager = CaptureManager(cv2.VideoCapture(0),self._windowManager,True)
		self._faceTracker = FaceTracker()
		self._shouldDrawDebugRects = False
		self._curveFilter = filters.BGRPortraCurveFilter()

	def run(self):
		"""run the main loop"""
		self._windowManager.createWindow()
		while  self._windowManager.isWindowCreated:
			self._captureManager.enterFrame()
			frame = self._captureManager.frame

			self._faceTracker.update(frame)
			faces = self._faceTracker.faces
			rects.swapRects(frame,frame,
				[face.faceRect for face in faces])


			#TODO:Filter the frame
			filters.strokeEdges(frame,frame)
			self._curveFilter.apply(frame,frame)

			if self._shouldDrawDebugRects:
				self._faceTracker.drawDebugRects(frame)

			self._captureManager.exitFrame()
			self._windowManager.processEvents()

	def onKeypress(self,keycode):
		"""Handle a keypress
		space -> Take a screenshot
		tab -> Start/Stop recording a screencast
		x -> Start/Stop drawing debug rectangles around faces.
		escape -> Quit
		"""
		if keycode == 32:#space
			self._captureManager.writeImage('screenshot.png')
		elif keycode == 9: #tab
			if not self._captureManager.isWritingVideo:
				self._captureManager.startWritingVideo('screencast.avi')
			else:
				self._captureManager.stopWritingVideo()
		elif  keycode == 120: #x
			print "x"
			self._shouldDrawDebugRects = \
			not self._shouldDrawDebugRects
			print self._shouldDrawDebugRects
		elif keycode == 27: #escape
			self._windowManager.destoryWindow()


class CameoDouble(Cameo):
	def __init__(self):
		Cameo.__init__(self)
		self._hiddenCaptureManager = CaptureManager(cv2.VideoCapture(1))

	def run(self):
		"""run the main loop"""
		self._windowManager.createWindow()
		while  self._windowManager.isWindowCreated:
			self._captureManager.enterFrame()
			self._hiddenCaptureManager.enterFrame()
			frame = self._captureManager.frame
			hiddenFaces = self._hiddenCaptureManager.frame
			self._faceTracker.update(hiddenframe)
			faces = self._faceTracker.faces

			i=0
			while i<len(faces) and i<len(hiddenFaces):
				rects.copyRect(hiddenframe,frame,hiddenFaces[i].faceEct,
				faces[i].faceRect)
				i +=1	


			#TODO:Filter the frame
			filters.strokeEdges(frame,frame)
			self._curveFilter.apply(frame,frame)

			if self._shouldDrawDebugRects:
				self._faceTracker.drawDebugRects(frame)

			self._captureManager.exitFrame()
			self._hiddenCaptureManager.exitFrame()
			self._windowManager.processEvents()

if __name__ == "__main__":
	Cameo().run()
	#CameoDouble.run() #for double camra