import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize webcam
cap = cv2.VideoCapture(0)

# Create a window and make it resizable
cv2.namedWindow("CVZone Finger Counter", cv2.WINDOW_NORMAL)
# Yahan aap apna manchaha size set kar sakte hain (e.g., 1280x720 ya 1920x1080)
cv2.resizeWindow("CVZone Finger Counter", 1280, 720)

# Initialize HandDetector
detector = HandDetector(staticMode=False, maxHands=1, detectionCon=0.8, minTrackCon=0.5)

while True:
    success, frame = cap.read()
    if not success:
        continue

    # 1. Unflipped frame detector ko dein taaki Left/Right accuracy bani rahe
    hands, processed_frame = detector.findHands(frame, draw=True)

    # 2. Frame ko horizontally flip karein natural mirror view ke liye
    processed_frame = cv2.flip(processed_frame, 1)

    total_fingers = 0

    if hands:
        hand1 = hands[0]
        # Auto finger status checklist
        fingers = detector.fingersUp(hand1)
        total_fingers = fingers.count(1)

    # --- UI SHIFT TO BOTTOM ---
    # Frame ki height nikal kar box ko niche shift kar rahe hain taaki top area clear rahe
    h, w, c = processed_frame.shape
    
    # Bottom Left corner me Box banayein
    cv2.rectangle(processed_frame, (20, h - 140), (320, h - 20), (0, 0, 0), cv2.FILLED)
    # Fingers count display text
    cv2.putText(
        processed_frame, f"Fingers: {total_fingers}", (40, h - 55), 
        cv2.FONT_HERSHEY_DUPLEX, 1.5, (0, 255, 0), 3
    )

    # Display the large window
    cv2.imshow("CVZone Finger Counter", processed_frame)

    # Press 'q' to exit instantly
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()