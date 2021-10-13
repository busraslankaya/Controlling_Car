
# Controlling Car with Image Processing  


I used the Opencv-Python library to realize the project. At first i wrote a code that 
instantly recognizes the hand i show in opencv. At the same time, this code shows us the 
numbers up to 5, which i show with my hands. The user's finger count contains commands 
to move the car. What i need to do to establish the connection between this code and the 
tool is to connect the arduino toolkit i purchased to the computer with the bluetooth module 
and enter the serial port of the arduino into the code we wrote. In this way, the commands 
corresponding to the hand movements i show when the camera is turned on will be 
transferred to the vehicle.

This is my arduino car:

![arduinocar](https://user-images.githubusercontent.com/60943616/137198167-21c73875-8991-426a-8578-107837dad67f.png)

The circuit diagram is as follows:

![circuitdiagram](https://user-images.githubusercontent.com/60943616/137198326-3222eec3-ff18-4844-88ba-bcfc1a1f6361.PNG)


MEDIAPIPE

MediaPipe offers customizable Python solutions as a prebuilt Python package on PyPI, which 
can be installed simply with pip install mediapipe . It also provides tools for users to build 
their own solutions. Mediapipe is widely used in many models such as face, hand, object 
recognition. Here, we have used all hand parameters by using the Mediapipe Hands functions.
MediaPipe Hands is a high quality hand and finger tracking solution. As seen in Figure 2, 
there are 21 landmarks on the hand. Mediapipe performs hand detection and tracking 
functions thanks to these landmarks. Two methods are used for these functions

![image](https://user-images.githubusercontent.com/60943616/137198557-8e679b54-36fb-42c3-b7da-2a90bde79578.png)


And finally, I prepared it with the tkinter library, the interface is like this:

![image](https://user-images.githubusercontent.com/60943616/137198642-b96b08d5-48e5-4c97-b28e-00812cd7ac16.png)


# What you need to do to run the code; 

Installing the opencv and mediapipe libraries. Install the tkinter library in the interface and run interface.py. Press the camera button. Show your right or left hand to the camera.
Also, after loading the arduino codes on your device, connect with python.

