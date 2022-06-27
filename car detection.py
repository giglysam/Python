import cv2

car_classifier = cv2.CascadeClassifier('haarcascade_car.xml')

cap = cv2.VideoCapture(0)

while cap.isOpened():

        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cars = car_classifier.detectMultiScale(gray, 1.2, 3)

        if len(cars) > 0:
            cv2.putText(frame, str(len(cars)), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            for (x, y, w, h) in cars:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)

        if cv2.waitKey(1) == 13:
            break

        cv2.imshow('Cars', frame)


cap.release()
cv2.destroyAllWindows()
