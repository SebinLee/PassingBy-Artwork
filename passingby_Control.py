import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("controlPanel.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #Initialize Current Value Text
        self.txtThreshold.setText(str(self.sliderThreshold.value()))
        self.txtCamera.setText(str(1.0/self.sliderCamera.value()))
        self.txtFrameRate.setText(str(self.sliderFrameRate.value()))
        self.txtListSize.setText(str(self.sliderListSize.value()))

        #Link Functions to Slider
        self.sliderThreshold.valueChanged.connect(self.editThreshold)
        self.sliderCamera.valueChanged.connect(self.editCameraOpacity)
        self.sliderFrameRate.valueChanged.connect(self.editFrameRate)
        self.sliderListSize.valueChanged.connect(self.editListSize)

        
    def editThreshold(self) :
        self.txtThreshold.setText(str(self.sliderThreshold.value()))
        
    def editCameraOpacity(self) :
        self.txtCamera.setText(str(1.0/self.sliderCamera.value()))

    def editFrameRate(self) :
        self.txtFrameRate.setText(str(self.sliderFrameRate.value()))

    def editListSize(self) :
        self.txtListSize.setText(str(self.sliderListSize.value()))

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()