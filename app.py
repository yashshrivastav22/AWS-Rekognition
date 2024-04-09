from flask import Flask, request, render_template, jsonify
import boto3
app = Flask(__name__)
# AWS credentials
AWS_ACCESS_KEY_ID = 'AKIAYS2NXC35VLOOTJ6Q'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION = 'us-east-1'
# Initialize AWS Rekognition client
rekognition = boto3.client('rekognition', 
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name=AWS_REGION)
@app.route('/')
def index():
   return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload():
   if 'file' not in request.files:
       return jsonify({'error': 'No file part'}), 400
   
   file = request.files['file']
   if file.filename == '':
       return jsonify({'error': 'No selected file'}), 400
   # Perform video analysis
   try:
       response = rekognition.start_label_detection(
           Video={
               'S3Object': {
                   'Bucket': 'yashshrivastav-mybucket1',
                   'Name': 'video1.mp4'
               }
           }
       )
       job_id = response['JobId']
       return jsonify({'job_id': job_id}), 200
   except Exception as e:
       return jsonify({'error': str(e)}), 500
@app.route('/search', methods=['GET'])
def search():
   object_name = request.args.get('object_name')
   if not object_name:
       return jsonify({'error': 'Object name not provided'}), 400
   
   try:
       # Retrieve timestamps for object
       # Perform necessary operations to retrieve timestamps associated with object_name
       timestamps = []  # Dummy data, replace with actual logic
       return jsonify({'object_name': object_name, 'timestamps': timestamps}), 200
   except Exception as e:
       return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)
