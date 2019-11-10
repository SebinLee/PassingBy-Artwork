import cv2
import time
import numpy as np
import random

contourList = list()

#Make Contour coordinates from the Image and Add Infos to contourList List
def makeContours(frame, threshold, listsize) :

    """
    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) : frame을 Grayscale로 변환(색상변환)을 해주는 코드
    cv2.threshold(grayscaled_frame, boundary, maxValue, cv2.THRESH_BINARY) : Grayscale로 변환된 Frame을 Boundary 값을 기준으로 이진화 해주는 코드
    cv2.bitwise_not(frame) : frame을 반전시켜주는 코드
    cv2.findContours(binaryFrame, Options) : binaryframe에서 Contour 좌표값을 가져오는 코드
    cv2.blur(frame, (verticalBlur, HorizontalBlur)) : frame에 blur를 적용할 수 있는 코드
    """

    thresholdBoundary = threshold
    maxValue = 255

    grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(grayscale,thresholdBoundary,maxValue,cv2.THRESH_BINARY)
    binary = cv2.blur(binary,(10,10))
    contours, hierachy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    contours = sortContours(contours)
    color = makeColor()

    if(len(contourList) >= listsize) : contourList.pop(0)
    contourList.append((contours,color))

#Sort contours according to the number of coordinates and return 
def sortContours(contours) :
    
    lenContours = []
    addContours = []

    for i in contours : lenContours.append(len(i))

    for i in range(10) :
        try :
            index = lenContours.index(max(lenContours))
            tmpContour = contours.pop(index)
            addContours.append(tmpContour)
            lenContours.pop(index)

        except : break

    return addContours

#Make Contour Line Color
def makeColor() :
    red = random.randint(125,255)
    green = random.randint(125,255)
    blue = random.randint(125,255)

    return (blue, green, red)


def artwork(t_threshold, t_cameraOpacity, t_framerate, t_listsize, testMode):
    """
    OpenCV Python을 이용해 Camera에서 실시간 영상을 받아옵니다.
    - capture : 카메라에서 영상을 받아오는 객체
    - VideoCapture(n) : n번째 카메라의 영상을 받아옵니다.
    - set(cv2.CAP_PROP_FRAME_WIDTH(or HEIGHT),width) : 카메라의 해상도를 설정합니다.
    """
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

    framerate = t_framerate
    framerate_waittime= 1.0/framerate

    count = 0

    while True :
        if testMode == True :
            if count >= t_framerate * 5 : break
            count += 1

        ret, frame = capture.read()
        
        background = cv2.imread("blackScreen.jpg",cv2.IMREAD_ANYCOLOR)
        showImage = background.copy()

        if ret :
            makeContours(frame,t_threshold,t_listsize)

            print(len(contourList))
            for contourItem in contourList :

                overlayBackground = background.copy()
                for i in contourItem[0]: cv2.drawContours(overlayBackground, [i], 0, contourItem[1], 2)
                showImage = cv2.addWeighted(overlayBackground,0.5,showImage,0.8,0)


            showImage = cv2.addWeighted(showImage,1,frame,t_cameraOpacity,0)
            cv2.imshow("src", showImage)

        else :
            print("NO CAMERA DETECT")
            break

        time.sleep(framerate_waittime)

    capture.release()
    cv2.destroyAllWindows()