import cv2       #To use opencv
import winsound  #To help us make sound when some human being is moving
cam = cv2.VideoCapture(0)   #To initialsize the camera. Since we have a single camera therefore the value 0 will suffice otherwise we would have put the corresponding camera number.
while cam.isOpened():
    ret,frame1 = cam.read()                       #ret means retried and frame is to capture from the camera.
    ret,frame2 = cam.read()
    diff = cv2.absdiff(frame1,frame2)             #This variable stores difference between different frames.This difference is coloured but colorful images might have errors so to avoid that we will convert it to grey image.
    gray = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)  #To convert the above coloured image to grey image.
    blur = cv2.GaussianBlur(gray, (5,5),0)        #To conver the image into a bit of blurred image.
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)  #To have more shrper images by getting rid of noises and unwanted things. 
    dilated = cv2.dilate(thresh, None, iterations=3)  #To dilate the image
    contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  #To find contours or boxes around the objects.
    # cv2.drawContours(frame1,contours,-1,(0,255,0),2) #To draw contours on top of frame1.
    for c in contours:
        if cv2.contourArea(c) < 5000:                   #We are only looking for countours which are of specific area otherwise there will be lot of different countors even for any small disturbance.
            continue
        x,y,w,h=cv2.boundingRect(c)                          #Here we are getting coordinated of countors.
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)    #Here we are building rectangle around those countors.
        # winsound.Beep(500,200)
        winsound.PlaySound("C:/Users/212811098/Downloads/Security Camera/alert.wav" , winsound.SND_FILENAME | winsound.SND_ASYNC)  
                                                 #To raise the sound whenever the boxes are created and moving.winsound.SND_ASYNC will ensure that it while the sound is being 
                                          # raised the detection does not stop and both the processes work asynchronously.
    if cv2.waitKey(10)==ord('q'):                 #Just wait for 10ms and see if user has pressed key 'q' or not
        break                                  #Just close the window if the above condition stands true.
    cv2.imshow('My Camera',frame1)              #To show what the camera has captured.