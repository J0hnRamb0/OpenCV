import os 
import cv2 

image= cv2.imread("C:/Users/Jonathon/JetLearn/OpenCV/download.png", 1)
cv2.imshow("Original",image)
resized = cv2.resize(image,(15,15))
cv2.imshow("Smaller Scale Image", resized)

scaled = cv2.resize(image,(0,0), fx=1.5, fy=1.5)
cv2.imshow("Bigger Image", scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()