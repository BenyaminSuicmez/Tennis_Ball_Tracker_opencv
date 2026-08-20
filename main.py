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

    cv2.imshow("Video", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

