# import the necessary packages
from threading import Thread
import cv2
import time

class VideoCapture:
	def __init__(self, src=0):
		# initialize the video / camera stream
		self.stream = cv2.VideoCapture(src)
		(self.grabbed, self.frame) = self.stream.read()

		#for measuring FPS
		self.FPS = 0
		self.counter = 0
		self.st = time.time()
		self.passed_frame = None

		#indicate if the thread should be stopped
		self.stopped = False
		self.show_frames_thread_running = False

		#starting video capture thread as soon object is initialized
		t = Thread(target=self.update, name='read_stream', args=())
		t.daemon = True
		t.start()

	@property
	def fps(self):
		return self.FPS


	def resize(self, frame, width=600):
		(h, w) = frame.shape[:2]
		r = width / float(w)
		dim = (width, int(h * r))
		frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
		return frame


	def update(self):
		# keep looping infinitely until the thread is stopped
		while True:
			# if the thread indicator variable is set, stop the thread
			if self.stopped:
				break

			# otherwise, read the next frame from the stream
			(self.grabbed, self.frame) = self.stream.read()


	def imshow(self, title, frame, width=False):
		self.passed_frame = frame
		#if thread is already started pass
		if not self.show_frames_thread_running:
			args = (title, width)
			t1 = Thread(target=self.show_frames, name='show_frame', args=(args,))
			t1.daemon = True
			t1.start()


	def show_frames(self, args):
		self.show_frames_thread_running = True

		title, width = args
		while True:
			# if True top the thread
			if self.stopped:
				self.show_frames_thread_running = False
				break

			if width:#if width is given then resize
				frame = self.resize(self.passed_frame, width)
			else:
				frame = self.passed_frame

			#show the next frame from the stream
			cv2.imshow(title, frame)
			if cv2.waitKey(1) == ord('q'):
					self.stopped = True
					self.grabbed = False
					self.show_frames_thread_running = False

		self.show_frames_thread_running = False


	def read(self):
		self.counter+=1
		if (time.time() - self.st) > 1 :
			self.FPS = round(self.counter / (time.time() - self.st))
			self.counter = 0
			self.st = time.time()

		# return the frame most recently read
		return self.grabbed, self.frame


	def release(self):
		#indicates thread should be stopped
		self.stopped = True
