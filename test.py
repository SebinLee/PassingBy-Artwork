import cv2

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

while True :

    """
    capture.read() : Camera 객체로 부터 데이터를 가져옵니다.
    - ret : Camera가 Available한지를 Boolean의 형태로 알려줍니다.
    - frame : Camera의 데이터를 가져다줍니다.
    """

    try :
        ret, frame = capture.read()

        if ret :

            thresholdBoundary = 150
            maxValue = 255


            grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            _, binary = cv2.threshold(grayscale,thresholdBoundary,maxValue,cv2.THRESH_BINARY)
            binary = cv2.blur(binary,(10,10))
            #cv2.imshow("VideoThreshold",binary)

            contours, hierachy = cv2.findContours(binary,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

            for i in contours :
                #hull은 numpy.ndarray type이기 때문에 list()가 아니라 []로 변환한다.
                hull = [cv2.convexHull(i,clockwise = True)]

                #점들의 위치 정보는 hull[0]에 들어있기 때문에 hull[0]을 조사합니다.
                if len(hull[0]) > 5 :
                    cv2.drawContours(grayscale,hull,0,(0,0,255),2)

            cv2.imshow("Windows with Threshold",grayscale)
        
        else :
            print("NO CAMERA DETECT")
            break

        if cv2.waitKey(1) > 0 : break

    except :
        print("No Camera Detect - With Exception")
        break

print("CAPTURE END")
capture.release()
cv2.destroyAllWindows()