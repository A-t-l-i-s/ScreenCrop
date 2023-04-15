from engine.require import *
from engine.options import *

from .timerEvent import *
from .paintEvent import *





__all__=["Window"]





class Window(QMainWindow):



	timerEvent=timerEvent
	paintEvent=paintEvent



	MODE_HIDDEN=0
	MODE_SCREENSHOT=1
	MODE_EDIT=2
	MODE_DRAW=3



	def __init__(self):
		super().__init__()


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.fps=60

		self.screen=None
		self.screenGeometry=None
		self.screenCursor=Qt.CrossCursor
		
		self.screenMode=self.MODE_HIDDEN
		self.prevScreenMode=self.MODE_SCREENSHOT

		self.screenshotBox=QRect(0,0,0,0)





		# ~~~~~~~ Window Properties ~~~~~~
		self.setWindowTitle("ScreenCrop")
		self.setWindowIcon(Options.icon)

		self.setCursor(self.screenCursor)
		
		self.setGeometry(0,0,0,0)

		self.setAttribute(Qt.WA_TranslucentBackground,True)
		self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)





		# ~~~~~~~~~~ System Tray ~~~~~~~~~
		self.systemTray=QSystemTrayIcon(self)
		self.systemTray.setIcon(Options.icon)
		self.systemTray.activated.connect(self.onSystemTrayClick)



		self.systemTrayMenu=QMenu()
		self.systemTray.setContextMenu(self.systemTrayMenu)



		self.systemTrayMenu_open=QAction("Open")
		self.systemTrayMenu_open.triggered.connect(lambda:print("YOU CLICKED IT!!!"))
		self.systemTrayMenu.addAction(self.systemTrayMenu_open)


		self.systemTrayMenu_exit=QAction("Exit")
		self.systemTrayMenu_exit.triggered.connect(self.exit)
		self.systemTrayMenu.addAction(self.systemTrayMenu_exit)





		# ~~~~~~~~~~~~~ Timer ~~~~~~~~~~~~
		self.timer=QBasicTimer()
		self.timer.start(1000/self.fps,self)





		# ~~~~~~~~~ Global Hotkey ~~~~~~~~
		keyboard.add_hotkey(Options.hotkey,self.onHotkey)





		# ~~~~~~~~~~~~~ Show ~~~~~~~~~~~~~
		self.show()
		self.systemTray.show()







	def exit(self):
		self.setDisplay(True)
		Application.exit()





	def mousePressEvent(self,event):
		buttons=event.buttons()
		x,y=event.x(),event.y()

		if (buttons==Qt.LeftButton):
			if (self.screenMode==self.MODE_SCREENSHOT):

				self.screenshotBox.setX(x)
				self.screenshotBox.setY(y)

				self.screenshotBox.setWidth(0)
				self.screenshotBox.setHeight(0)

				self.setCursor(Qt.BlankCursor)





	def mouseReleaseEvent(self,event):
		buttons=event.buttons()
		x,y=event.x(),event.y()

		if (buttons==Qt.NoButton):
			if (self.screenMode==self.MODE_SCREENSHOT):
				self.setCursor(self.screenCursor)





	def mouseMoveEvent(self,event):
		buttons=event.buttons()
		x,y=event.x(),event.y()

		if (buttons==Qt.LeftButton):
			if (self.screenMode==self.MODE_SCREENSHOT):
				self.screenshotBox.setWidth(x-self.screenshotBox.x())
				self.screenshotBox.setHeight(y-self.screenshotBox.y())







	def onSystemTrayClick(self,event):
		if (event==QSystemTrayIcon.ActivationReason.Trigger):
			self.setDisplay(False)






	def onHotkey(self):
		self.setDisplay()





	def setDisplay(self,off=None):
		if (off==None):
			off=self.screenMode!=self.MODE_HIDDEN


		if (off):
			self.prevScreenMode=self.screenMode
			self.screenMode=self.MODE_HIDDEN
		else:
			self.screenMode=self.prevScreenMode








