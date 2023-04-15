from engine.require import *
from engine.options import *





__all__=["timerEvent"]





def timerEvent(self,event):
	
	screen=Application.screenAt(QCursor.pos())

	if (screen!=self.screen):
		self.screen=screen
		self.screenGeometry=self.screen.geometry()

		self.setGeometry(self.screenGeometry)



	self.repaint()



