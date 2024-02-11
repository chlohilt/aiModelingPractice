import cv2

# Access the webcam
cap = cv2.VideoCapture(0)  # 0 is the default index for the primary webcam

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Capture a frame from the webcam
ret, frame = cap.read()

if not ret:
    print("Error: Could not capture frame.")
    exit()

# Display the captured frame
cv2.imshow('Webcam', frame)

# Save the captured frame to a file
cv2.imwrite('captured_image.jpg', frame)

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()