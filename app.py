from flask import Flask, render_template, jsonify
from threading import Thread
import cv2
import boto3
import time

# AWS Configuration
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_REGION = ''

# Initialize AWS Rekognition client
rekognition = boto3.client('rekognition', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION)

# Function to detect objects using Rekognition
def detect_objects(frame):
    # Convert frame to bytes
    _, img_encoded = cv2.imencode('.jpg', frame)
    img_bytes = img_encoded.tobytes()

    # Detect objects using Rekognition
    response = rekognition.detect_labels(Image={'Bytes': img_bytes}, MaxLabels=10)

    # Extract detected objects
    objects = [label['Name'] for label in response['Labels']]
    return objects

# Function to capture frames from the camera and send detected objects to the web application
def camera_thread():
    app = Flask(__name__)

    # Initialize variables for timeline
    timeline = []

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/objects')
    def objects():
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        # Process frame and detect objects
        objects_detected = detect_objects(frame)

        # Add detected objects and timestamp to the timeline
        timeline.append({'timestamp': time.time(), 'objects': objects_detected})

        return jsonify({'objects': objects_detected})

    @app.route('/timeline')
    def get_timeline():
        return jsonify({'timeline': timeline})

    app.run()

if __name__ == "__main__":
    # Start camera thread
    camera_thread()