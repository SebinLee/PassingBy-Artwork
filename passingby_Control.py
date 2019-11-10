import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import passingby_Artwork
import threading

form_class = uic.loadUiType("controlPanel.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.threshold = self.sliderThreshold.value()
        self.cameraOpacity = float(self.sliderCamera.value())/100
        self.framerate = self.sliderFrameRate.value()
        self.listsize = self.sliderListSize.value()


        #Initialize Current Value Text
        self.txtThreshold.setText(str(self.threshold))
        self.txtCamera.setText(str(self.cameraOpacity))
        self.txtFrameRate.setText(str(self.framerate))
        self.txtListSize.setText(str(self.listsize))

        #Link Functions to Slider
        self.sliderThreshold.valueChanged.connect(self.editThreshold)
        self.sliderCamera.valueChanged.connect(self.editCameraOpacity)
        self.sliderFrameRate.valueChanged.connect(self.editFrameRate)
        self.sliderListSize.valueChanged.connect(self.editListSize)

        self.btnStart.clicked.connect(self.startArtwork)
        self.btnTest.clicked.connect(self.testArtwork)
        
    def editThreshold(self) :
        self.txtThreshold.setText(str(self.sliderThreshold.value()))
        self.threshold = self.sliderThreshold.value()
        
    def editCameraOpacity(self) :
        self.txtCamera.setText(str(1.0/self.sliderCamera.value()))
        self.cameraOpacity = float(self.sliderCamera.value())/100
        
    def editFrameRate(self) :
        self.txtFrameRate.setText(str(self.sliderFrameRate.value()))
        self.framerate = self.sliderFrameRate.value()

    def editListSize(self) :
        self.txtListSize.setText(str(self.sliderListSize.value()))
        self.listsize = self.sliderListSize.value()

    def startArtwork(self) :
        passingby_Artwork.artwork(self.threshold, self.cameraOpacity, self.framerate, self.listsize,False)

    def testArtwork(self) :
        passingby_Artwork.artwork(self.threshold, self.cameraOpacity, self.framerate, self.listsize,True)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 