import cv2
import os

xml_path = os.path.join(os.getcwd(), 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(xml_path)

print("XML Path:", xml_path)
print("Loaded:", not face_cascade.empty())

img = cv2.imread('sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()