from engine.require import *
from engine.options import *





__all__=["paintEvent"]





def paintEvent(self,event):
	painter=QPainter(self)


	if (self.screenMode!=self.MODE_HIDDEN):
		if (self.screenMode==self.MODE_SCREENSHOT):
			if (self.screenGeometry):
				# Fill background
				painter.fillRect(
					0,0,
					self.screenGeometry.width(),
					self.screenGeometry.height(),
					Options.screenshotBackgroundColor
				)


				# Draw rect box
				painter.setPen(
					QPen(
						Options.screenshotBoxColor,
						Options.screenshotBoxWidth
					)
				)
				painter.drawRect(self.screenshotBox)


	painter.end()



