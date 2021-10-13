import cv2
import mediapipe as mp
import serial

Arduino_Serial = serial.Serial('com5',9600)  #Create Serial port object called arduinoSerialData
#opencamera 
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

oldValue = 0

#HAND DETECTION
class handGesture():
    #Ititializes a Mediapipe hand object
    def __init__(self, static_image_mode=False, max_num_hands=2, min_detection_con=0.5, min_tracking_con=0.5):
        self.mode = static_image_mode
        self.maxHands = max_num_hands
        self.detectionCon = min_detection_con
        self.trackCon = min_tracking_con
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def drawHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
     
        if self.results.multi_hand_landmarks:
            for each_handLms in self.results.multi_hand_landmarks:
                if draw: #red point and green lines
                    self.mpDraw.draw_landmarks(img, each_handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def positions(self, img, handNo=0):
        #landmarks numbers list
        lmsList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lms in enumerate(myHand.landmark):
                h, w, c = img.shape #height, weight, channels
                cx, cy = int(lms.x * w), int(lms.y * h)
                lmsList.append([id, cx, cy])

        return lmsList
#FINGER COUNTER

#hand landmarks num
tipIds = [4, 8, 12, 16, 20]
detection = handGesture(min_detection_con=0.75)
while True:
    success, img = cap.read()
    img = detection.drawHands(img)
    lmsList = detection.positions(img)

    if len(lmsList) != 0:
        fingers = []
        if( lmsList[tipIds[1]][1] > lmsList[tipIds[4]][1]):
            # Right Thumb
            if lmsList[tipIds[0]][1] > lmsList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Right 4 Fingers
            for id in range(1, 5):
                if lmsList[tipIds[id]][2] < lmsList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            fingerNum = fingers.count(1)

        if( lmsList[tipIds[1]][1] < lmsList[tipIds[4]][1]):
            # Left Thumb
            if lmsList[tipIds[0]][1] < lmsList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Left 4 Fingers
            for id in range(1, 5):
                if lmsList[tipIds[id]][2] < lmsList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            fingerNum = fingers.count(1)
    
        #sending data to Arduino
        newValue = fingerNum
        if(newValue!=oldValue):
            sent=False
            oldValue=newValue 
            
        if(not sent):
            if newValue==5:
                Arduino_Serial.write(b'5')
                print("5 Verisi yollandı")
            elif newValue==1:
                Arduino_Serial.write(b'1')
                print("1 Verisi yollandı")
            elif newValue==2:
                Arduino_Serial.write(b'2')
                print("2 Verisi yollandı")
            elif newValue==3:
                Arduino_Serial.write(b'3')
                print("3 Verisi yollandı")
            elif newValue==4:
                Arduino_Serial.write(b'4')
                print("4 Verisi yollandı")
            sent=True 

        cv2.putText(img, str(fingerNum), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    8, (0, 0, 0), 5)

        if newValue==5:
            cv2.putText(img, "stop", (20, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    2, (0, 0, 0), 4)
            print(fingerNum , "stop")
        if newValue==1:    
            cv2.putText(img, "forward", (20, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    2, (0, 0, 0), 4)
            print(fingerNum , "forward")
        if newValue==2:
            cv2.putText(img, "backward", (20, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    2, (0, 0, 0), 4)
            print(fingerNum , "backward")
        if newValue==3:
            cv2.putText(img, "right", (20, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    2, (0, 0, 0), 4)  
            print(fingerNum , "right") 
        if newValue==4:
            cv2.putText(img, "left", (20, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    2, (0, 0, 0), 4) 
            print(fingerNum , "left")   
        
    cv2.imshow("Image", img)
    cv2.waitKey(1)
