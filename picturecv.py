import cv2

face_hear_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.inread('gideon_pic.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)




faces = face_haar_cascade.detectMultiscale(gray, 1.3, 5)


for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 270,0),12
                  )
    cv2.imshow("faces", image)
    cv2.waitkey()