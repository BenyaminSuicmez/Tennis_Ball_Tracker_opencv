import cv2



# HSV range for the tennis ball, measured via manual sampling
lower = (20, 120, 100)
upper = (35, 255, 255)



cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break 


    frame = cv2.flip(frame, flipCode=1)

    hsv = cv2.cvtColor(frame, code=cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lowerb=lower, upperb=upper)



    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:

        biggest = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(biggest)

        cv2.rectangle(frame, pt1=(x, y), pt2=(x+w, y+h), color=(0, 255, 0), thickness=4)

        cv2.putText(frame, "Tennis Ball", org=(x, y-10), fontFace=cv2.FONT_HERSHEY_COMPLEX, color=(0,255, 0), fontScale=2)

    cv2.imshow("Tracker", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

