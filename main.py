import cv2


# face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
mask_detector = cv2.CascadeClassifier('mask.xml')

webcam = cv2.VideoCapture(0)

while True:
    #Read current frame from webcam
    successful_frame, frame = webcam.read()

    # If there's an error, abort
    if not successful_frame:
        break

    #Change to grayscale
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect faces first
    mask = mask_detector.detectMultiScale(frame_grayscale)
    

    #Run smile detection within each of those faces
    for (x,y,w,h) in mask:
        #Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 200, 50), 4)
        
  
    #show the current frame
    cv2.imshow('mask Detector', frame)

    #Display
    key=cv2.waitKey(1)

    #Stop if Q key is pressed
    if key==81 or key==113:
        break

#CleanUP    
webcam.release()
cv2.destroyAllWindows()


print("completed")