from Engine.Require import *

from .timerEvent import *
from .paintEvent import *





__all__=["Window"]





class Window(QMainWindow):


	timerEvent=timerEvent
	paintEvent=paintEvent


	def __init__(self):
		super().__init__()


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.screen=None
		self.screenGeometry=None

		self.cursor=Qt.CrossCursor

		self.fps=60



		# ~~~~~~~ Window Properties ~~~~~~
		self.setWindowTitle("ScreenCrop")
		self.setCursor(self.cursor)
		
		self.setGeometry(0,0,0,0)

		self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
		self.setAttribute(Qt.WA_TranslucentBackground,True)



		# ~~~~~~~~~~~~ Widgets ~~~~~~~~~~~
		self.timer=QBasicTimer()
		self.timer.start(1000/self.fps,self)




