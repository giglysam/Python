import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

bw_threshold = 80

font = cv2.FONT_HERSHEY_SIMPLEX
org = (30, 30)
weared_mask_font_color = (255, 255, 255)
thickness = 2
font_scale = 1

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()

    img = cv2.resize(img, (294, 172))

    o = cv2.imread('images.png')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    (thresh, black_and_white) = cv2.threshold(gray, bw_threshold, 255, cv2.THRESH_BINARY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        cv2.putText(img, str(len(faces)), org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
        cv2.imshow('security camera', img)
    elif len(faces) == 0:
        cv2.imshow('security camera', o)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

