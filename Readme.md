## imstream [![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

The most exciting and powerful ``video /  webcam`` streamer for python it is built on top of OpenCV and threading module. It provides ultra fast *FPS ``400+`` when streamed.

````python
>> pip install imstream
````

### How it is possible

well you know ``cap.read()`` function in opencv is a blocking function it blocks your main loop i.e, it takes time to read the next frame, again ``cv2.imshow()`` takes time to show the frames and finally ``cv2.waitKey()`` also adds up a little bit of delay. In short all these functions are time consuming and makes your main loop slow.

So to tackle this problem what we are doing is:

- Reading the Next frames on a separate thread
- Returning the fames to our main loop
- processing the frames in our main loop
- showing the processed frame on different thread

Now you understand all the time consuming functions has been moved to separate thread so it is much easier for our main loop to process the frames one after another without waiting to received the frames or to show the frames.

### Advantage

Using this module is very easy, you just need to import the imstream module and use all the opencv dedicated functions for reading and showing frames with imstream.

| OpenCV                      | imstream                               |
| --------------------------- | -------------------------------------- |
| cap = cv2.VideoCapture(0)   | cap = imstream.VideoCapture(0)         |
| success, frame = cap.read() | success, frame = cap.read()            |
| cv2.imshow('camera', frame) | cap.imshow('camera', frame)            |
| -                           | print(cap.fps)                         |
| -                           | frame = cap.resize(frame, width=600)   |
| -                           | cap.imshow('camera', frame, width=400) |
| cv2.waitKey(1)              | Built in                               |

### Example

#### Let's try to read the camera with OpenCV

````python
import cv2
import time

cap = cv2.VideoCapture(0)

FPS = 0
counter = 0
st = time.time()
while True:
    success, frame = cap.read()

    if not success: break

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
````

Output

````python
.
.
.
FPS: 29
FPS: 30
FPS: 30
````

#### Now Let's read it with imstream

````python
import imstream

cap = imstream.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success: break

    print(f'FPS: {cap.fps}')

    cap.imshow('webcam', frame)

# do a bit of cleanup
cap.release()
````

Output

````python
.
.
.
FPS: 3866
FPS: 3880
FPS: 3880
````

Woah! I didn't believed on my eyes, well it's True. 

Note:- If you are showing frames you can terminate is by pressing ``q`` key on your keyboard.

**I was running this Test on:**

- Lenovo Think Pad X240
- Windows 10 Pro
- Intel Core i7-4600U
- 8GB RAM

#### Things to take care of

OpenCV is a dependency for imstream but since most of the times everyone uses different distribution of OpenCV i didn't mentioned it in the ``install_requires``. but if you face any problem like `Import Error: No Module Name cv2` , you can install it manually.

````python
>> pip install opencv-contrib-python
````

#### Citation

A big thanks to [Adrian Rosebrock](https://twitter.com/PyImageSearch) , Author of biggest Computer Vision blog online [PyimageSearch](https://www.pyimagesearch.com/). This module is built with the code snippets of [imutils](https://pypi.org/project/imutils/) library.

