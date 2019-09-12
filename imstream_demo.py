import cv2
import time
import imstream

#with multi threading
cap = imstream.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        break

    print(f'FPS: {cap.fps}')

    cap.imshow('webcam', frame)

# do a bit of cleanup
cap.release()


'''
#without multi threading
cap = cv2.VideoCapture(0)

FPS = 0
counter = 0
st = time.time()
while True:
    success, frame = cap.read()

    if not success:
        break

    counter+=1
    if (time.time() - st) > 1 :
        FPS = round(counter / (time.time() - st))
        counter = 0
        st = time.time()
    
    print(f'FPS: {FPS}')
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# do a bit of cleanup
cap.release()
'''