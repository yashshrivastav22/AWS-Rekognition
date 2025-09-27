# 🔒 AWS Rekognition Video Analysis to Alert Users in Cases of Visual Hacking

## 📌 Overview
Visual hacking also called **visual data breach** or **visual eavesdropping** is the unauthorized access of sensitive information by observing someone’s screen or surroundings. With remote work and video calls everywhere, it’s easier than ever for sensitive content to be exposed.

This project is a **Flask-based web app** that uses **AWS Rekognition** to analyze frames from the laptop webcam and highlight **potential risks** (e.g., unauthorized people, recording devices, documents). Detected labels are shown in the UI so users can take action.

---

## 🚀 Features
- 🎥 Capture webcam frames locally and analyze them with **AWS Rekognition**.
- 🧠 Display **detected object labels** in the web app.
- 🕒 Lightweight timeline endpoint to fetch recent detections (for UI updates).
- ⚡ Designed to run on a developer laptop for quick demos/POCs.

---

## 🏗️ Architecture
The system works by capturing webcam frames, sending them to **AWS Rekognition** for analysis, and returning object labels to the user through the Flask interface.

![Architecture Diagram](https://github.com/yashshrivastav22/Images/blob/main/AWS-Rekognition/Final_Diagram.jpg)

## 🛠️ Tech Stack
- **Backend:** Python, Flask  
- **Computer Vision:** AWS Rekognition (Video Analysis)  
- **Frontend:** HTML, CSS (Flask templates)  
- **Cloud:** AWS (Rekognition)  

---

## 📂 Project Structure

```
AWS-Rekognition/
│── app.py # Flask server, camera capture, Rekognition calls, endpoints
│── templates/
│ └── index.html # Minimal UI for viewing detections
│ └── Final_Diagram.jpg # System architecture diagram
│── README.md # This file
```

---

## ⚙️ Prerequisites
- Python 3.9+  
- An **AWS account** with Rekognition enabled  
- An IAM user/role with permission to call:
  - `rekognition:DetectLabels`
- A working **webcam**

> ✅ The app sends image bytes directly to Rekognition and renders labels in the UI.

---

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yashshrivastav22/AWS-Rekognition.git
   cd AWS-Rekognition/
   ```
2. **Create & activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```
3. **Manually install required modules**
   ```bash
   pip install flask boto3 opencv-python
   ```
  - `flask` → web server & templates
  - `boto3` → AWS SDK to call Rekognition
  - `opencv-python` → capture frames from webcam
4. **Configure AWS credentials & Region**
   Choose one of the following:
   - AWS CLI (recommended)
   ```bash
   aws configure
   ```
   - Environment variables
    ```bash
    export AWS_ACCESS_KEY_ID=YOUR_KEY
    export AWS_SECRET_ACCESS_KEY=YOUR_SECRET
    export AWS_DEFAULT_REGION=us-east-1
    ```
   - Or update the placeholders in `app.py` if you prefer hard-coding (not recommended).

5. **Run the Flask app**
   ```bash
   python app.py
   ```

6. **Open your browser and navigate to:**
   ```cpp
   http://127.0.0.1:5000
   ```
---

## 🎯 Usage

- Load the homepage to start/monitor detection results.
- The app captures frames locally, sends image bytes to Rekognition (`DetectLabels`), and displays labels returned by the API.
- Use the timeline endpoint in the UI (or via JS polling) to show recent detections.

---

## 🔐 Security Considerations

- Keep your AWS credentials secure (prefer environment variables or a credentials profile).
- Use least-privilege IAM policies (only `rekognition:DetectLabels`).
- This demo processes frames locally and sends only the image bytes used for label detection to Rekognition.
- For production: consider regional restrictions, network egress controls, encryption in transit, and consent for camera usage.

---

## 🧩 Troubleshooting
- If OpenCV fails to access the camera on Linux:
```bash
sudo apt-get update && sudo apt-get install -y libgl1
```
- Ensure your webcam is not in use by another application.
- Verify `AWS_DEFAULT_REGION` matches a region where Rekognition is available.

## 📚 References

- [Amazon Rekognition - DetectLabels](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html)
- [Boto3 Rekognition Client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html)
- [Flask Documentation](https://flask.palletsprojects.com/en/stable/)

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.
