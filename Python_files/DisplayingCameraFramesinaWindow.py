import cv2
import numpy

clicked = False

def onMouse(event,x,y,flags,param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True
    
cameracapture = cv2.VideoCapture(0)
cv2.namedWindow('Window')
cv2.setMouseCallback('Window',onMouse)

print('Showing camera feed ')

success , frame = cameracapture.read()

while success  and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('Window',frame)
    success , frame = cameracapture.read()

#the argument for waitKey() is number of milliseconds to wait for keyboard and -1 is returned if no key is pressed

cv2.destroyAllWindows()
cameracapture.release()