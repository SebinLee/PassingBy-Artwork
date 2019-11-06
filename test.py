import cv2
import time

"""
OpenCV Python을 이용해 Camera에서 실시간 영상을 받아옵니다.
- capture : 카메라에서 영상을 받아오는 객체
- VideoCapture(n) : n번째 카메라의 영상을 받아옵니다.
- set(cv2.CAP_PROP_FRAME_WIDTH(or HEIGHT),width) : 카메라의 해상도를 설정합니다.
"""
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

trieditonce = False

framerate = 30
framerate_waittime= 1.0/framerate

while True :

    """
    capture.read() : Camera 객체로 부터 데이터를 가져옵니다.
    - ret : Camera가 Available한지를 Boolean의 형태로 알려줍니다.
    - frame : Camera의 데이터를 가져다줍니다.
    """

    ret, frame = capture.read()

    if ret :

        thresholdBoundary = 150
        maxValue = 255

        """
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) : frame을 Grayscale로 변환(색상변환)을 해주는 코드
        cv2.threshold(grayscaled_frame, boundary, maxValue, cv2.THRESH_BINARY) : Grayscale로 변환된 Frame을 Boundary 값을 기준으로 이진화 해주는 코드
        cv2.bitwise_not(frame) : frame을 반전시켜주는 코드
        cv2.findContours(binaryFrame, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE) : binaryframe에서 Contour 좌표값을 가져오는 코드
        """

        grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(grayscale,thresholdBoundary,maxValue,cv2.THRESH_BINARY)
        binary = cv2.bitwise_not(binary)
        contours, hierachy = cv2.findContours(binary,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)


        for i in range(len(contours)) : cv2.drawContours(grayscale, [contours[i]], 0, (0, 0, 255), 2)
        cv2.imshow("src", grayscale)

    
    else :
        print("NO CAMERA DETECT")
        break

    if cv2.waitKey(1) > 0 : break

    time.sleep(framerate_waittime)


print("CAPTURE END")
capture.release()
cv2.destroyAllWindows()