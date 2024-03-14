import sys
import os
import ctypes
import ntpath
import keyboard

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QMainWindow

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *

from RFTLib.Config import *
from RFTLib.Config.qt import *
from RFTLib.Config.yaml import *



# Intialize qt app
Application = QApplication([])



# Data structure
Data_Obj = RFT_Config(
	"./data",
	RFT_Config_YAML
)
Data = Data_Obj.data
Data.elevate("Data")


# Icons structure
Icons_Obj = RFT_Config(
	"./icons",
	RFT_Config_QT_ICON
)
Icons = Icons_Obj.data
Icons.elevate("Data")


# Images structure
Images_Obj = RFT_Config(
	"./images",
	RFT_Config_QT_IMAGE
)
Images = Images_Obj.data
Images.elevate("Images")


