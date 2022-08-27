from Engine.Require import *





__all__=["timerEvent"]





def timerEvent(self,event):
	
	screen=app.screenAt(QCursor.pos())

	if (screen!=self.screen):
		self.screen=screen
		self.screenGeometry=self.screen.geometry()

		self.setGeometry(
			self.screenGeometry.x(),
			self.screenGeometry.y(),
			self.screenGeometry.width(),
			self.screenGeometry.height()
		)



	self.repaint()




