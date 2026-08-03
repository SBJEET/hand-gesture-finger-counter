from flask import Flask, render_template, Response, jsonify
import cv2
from cvzone.HandTrackingModule import HandDetector

app = Flask(__name__)

detector = HandDetector(staticMode=False, maxHands=2, detectionCon=0.8, minTrackCon=0.6)
cap = cv2.VideoCapture(0)

hand_stats = {"right": 0, "left": 0, "total": 0}

def generate_frames():
    global hand_stats
    finger_tips = [8, 12, 16, 20] 

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame = cv2.flip(frame, 1)
            
            hands, processed_frame = detector.findHands(frame, draw=True)

            right_count = 0
            left_count = 0

            if hands:
                if len(hands) == 2:
                    hands = sorted(hands, key=lambda x: x["center"][0])

                for index, hand in enumerate(hands):
                    lmList = hand["lmList"]
                    if len(lmList) >= 21:
                        up_fingers = 0

 
                        if len(hands) == 2:
                            is_left_screen_hand = (index == 0)
                        else:
                            is_left_screen_hand = (hand["type"] == "Left")

                        if is_left_screen_hand:
                            if lmList[4][0] > lmList[2][0]: 
                                up_fingers += 1
                        else:
                            if lmList[4][0] < lmList[2][0]:
                                up_fingers += 1

                        for tip in finger_tips:
                            if lmList[tip][1] < lmList[tip - 2][1]: 
                                up_fingers += 1

                        if len(hands) == 2:
                            if index == 0:
                                left_count = up_fingers
                            else:
                                right_count = up_fingers
                        else:
                            if hand["type"] == "Left":
                                left_count = up_fingers
                            else:
                                right_count = up_fingers

            hand_stats["right"] = right_count
            hand_stats["left"] = left_count
            hand_stats["total"] = right_count + left_count

            ret, buffer = cv2.imencode('.jpg', processed_frame)
            processed_frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + processed_frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stats')
def stats():
    return jsonify(hand_stats)

if __name__ == "__main__":
    app.run(debug=True)