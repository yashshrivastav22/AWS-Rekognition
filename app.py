from flask import Flask, request, render_template, jsonify
import boto3
import uuid

app = Flask(__name__)

# AWS credentials
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_REGION = 'us-east-1'

# Initialize AWS Rekognition client
rekognition = boto3.client('rekognition',
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name=AWS_REGION)

# Initialize AWS S3 client
s3 = boto3.client('s3',
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

   try:
       # Generate a unique file key using UUID
       file_key = 'upload/' + str(uuid.uuid4()) + '.mp4'

       # Upload video to S3
       bucket_name = 'yashshrivastav-mybucket1'
       s3.upload_fileobj(file, bucket_name, file_key)

       # Perform video analysis with AWS Rekognition
       response = rekognition.start_label_detection(
           Video={
               'S3Object': {
                   'Bucket': bucket_name,
                   'Name': file_key
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
