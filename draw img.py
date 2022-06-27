import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)

    median = cv2.medianBlur(gray, 3)

    canny = cv2.Canny(median, 100, 200)

    points = np.argwhere(canny > 0)

    center, radius = cv2.minEnclosingCircle(points)

    cv2.imshow("canny", canny)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
