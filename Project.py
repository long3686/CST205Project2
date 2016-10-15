import cv2
import numpy as np
# Get user supplied values
# Create the haar cascade (define the path to the face detector)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#Set the webcam
cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()
	
	# Read the image
	# convert the image to grayscale, load the face cascade detector,
	# and detect faces in the image
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	
	# Draw a rectangle around the faces
	for(x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
	# Draw a rectangle around the eyes
		for (ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)

	# Display the resulting frame
	cv2.imshow('img', img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
# When everything done, release the capture
cap.release()
cv2. destroyAllWindows()