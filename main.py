import cv2

# Load test image
img = cv2.imread("ball.png")                      

# Convert to HSV for color-based detection
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)         

# HSV range for the tennis ball, measured via manual sampling below
lower = (20, 120, 100)
upper = (35, 255, 255)

def show_color(event, x, y, flags, param):
     # Only react to left-clicks
    if event == cv2.EVENT_LBUTTONDOWN:            
        print("Click at:", x, y)

        # Print HSV value at clicked pixel
        print("HSV-Value:", hsv[y, x])             

cv2.imshow("Ball", img)

# Attach click handler to the window
cv2.setMouseCallback("Ball", show_color)           
cv2.waitKey(0)
cv2.destroyAllWindows()

# cap = cv2.VideoCapture(0)


'''while True:
    ret, frame = cap.read()

    if not ret:
        break 


    frame = cv2.flip(frame, flipCode=1)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
'''
# cv2.destroyAllWindows()

