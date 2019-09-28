import cv2
import numpy

cameraCapture = cv2.VideoCapture(0)
fps = 30
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videowriter = cv2.VideoWriter('test1.avi',cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)

success , frame = cameraCapture.read()

numFramesRemaining = fps*10 -1 

while success and numFramesRemaining > 0:
    videowriter.write(frame)
    success , frame = cameraCapture.read()
    numFramesRemaining -=1

cameraCapture.release()

'''
    For a set of cameras we use grab() and retrieve()

    success0 = cameraCapture0.grab()
    success1 = cameraCapture1.grab()
    if success0 and success1:
        frame0 = cameraCapture0.retrieve()
        frame1 = cameraCapture1.retrieve()
'''