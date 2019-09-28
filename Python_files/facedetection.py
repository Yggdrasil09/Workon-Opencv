import cv2
from os.path import realpath, normpath


path = normpath(realpath(cv2.__file__) + '../../../../../share/OpenCV/haarcascades')

filename = './spock.jpg'

def detect(filename):
    face_cascade = cv2.CascadeClassifier(path + '/haarcascade_frontalface_default.xml')

    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.namedWindow('Face Detection')
    cv2.imshow('Face Detection',img)
    cv2.imwrite('./test.jpg',img)
    cv2.waitKey(0)

detect(filename)

