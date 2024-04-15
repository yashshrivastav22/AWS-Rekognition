from flask import Flask, request, render_template, jsonify, redirect, url_for
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
        return redirect(url_for('search', job_id=job_id))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        job_id = request.form['job_id']
        object_name = request.form['object_name']

        try:
            # Retrieve analysis results for the specified job_id
            response = rekognition.get_label_detection(JobId=job_id)
            detected_objects = []

            # Extract object details from the analysis results
            for label in response['Labels']:
                detected_objects.append({
                    'Name': label['Label']['Name'],
                    'Timestamp': label['Timestamp'] / 1000
                })


            # Filter detected objects based on the specified object_name
            filtered_objects = [obj for obj in detected_objects if obj['Name'].lower() == object_name.lower()]

            if not filtered_objects:
                return render_template('object_not_found.html', object_name=object_name)

            # Print all detected objects and their timestamps
            for obj in detected_objects:
                print(f"Object: {obj['Name']}, Timestamp: {obj['Timestamp']}")

            return render_template('search_results.html', object_name=object_name, detected_objects=filtered_objects)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        job_id = request.args.get('job_id')
        return render_template('search.html', job_id=job_id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
