from flask import Flask, render_template, Response
import cv2
import mediapipe as mp

app = Flask(__name__)

# Mediapipe init
mp_pose = mp.solutions.pose
mp_face = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/problem')
def problem():
    return render_template('problem.html')

@app.route('/solution')
def solution():
    return render_template('solution.html')

@app.route('/health')
def health():
    return render_template('health_scan.html')

@app.route('/factory')
def factory():
    return render_template('factory_monitor.html')

@app.route('/school')
def school():
    return render_template('school_monitor.html')

@app.route('/college')
def college():
    return render_template('college_monitor.html')

@app.route('/sign')
def sign():
    return render_template('sign_language.html')

@app.route('/advanced')
def advanced():
    return render_template('advanced_health.html')

@app.route('/whisper')
def whisper():
    return render_template('whisper_voice.html')

@app.route('/tech')
def tech():
    return render_template('tech_stack.html')

@app.route('/investment')
def investment():
    return render_template('investment.html')

# Video feed for factory/school
def gen_video():
    cap = cv2.VideoCapture(0)
    pose = mp_pose.Pose(min_detection_confidence=0.5)
    while True:
        ret, frame = cap.read()
        if not ret: break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = pose.process(rgb)
        if res.pose_landmarks:
            mp_drawing.draw_landmarks(frame, res.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2))
        _, buf = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buf.tobytes() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
