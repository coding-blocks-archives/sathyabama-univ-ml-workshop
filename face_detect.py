import cv2


img = cv2.imread('Before.png')
camera = cv2.VideoCapture(0)
#cv2.imshow("Image ",img)

face_detector = cv2.CascadeClassifier('my_model.xml')

while True:
	ret, img = camera.read()

	if ret==False:
		continue

	faces_detected = face_detector.detectMultiScale(img,1.3,5)
	for f in faces_detected:
		x,y,w,h = f # f is of type (x,y,w,h)
		green_color = (0,255,255)
		cv2.rectangle(img,(x,y),(x+w,y+h),green_color,10)

	cv2.imshow("Image",img)
	cv2.waitKey(1)