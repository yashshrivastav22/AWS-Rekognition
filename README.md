# AWS Rekognition video analysis to alert users in cases of visual hacking

## Introduction
Visual hacking, also known as visual data breach or visual eavesdropping, refers to the unauthorized access of sensitive information by watching someone's screen or activities from a distance. With the widespread adoption of remote work and virtual meetings, visual hacking has become a significant concern for individuals and organizations handling confidential data. Malicious actors can exploit vulnerabilities in video conferencing systems or webcam feeds, including laptop cameras, to gain unauthorized access to sensitive information displayed on screens or present in the user's environment.
AWS Rekognition Video Analysis is a powerful tool that can be utilized to mitigate the risks associated with visual hacking. This service leverages advanced computer vision and machine learning techniques to analyze video streams in real-time, enabling the detection and identification of objects, people, and activities.
In this project, we propose a web-based application that integrates AWS Rekognition Video Analysis to continuously monitor the user's laptop camera feed and detect potential visual hacking threats. The application identifies objects in the user's background that could pose a security risk, such as unauthorized individuals, recording devices, or sensitive documents. Detected objects are displayed in a Flask web application, allowing users to take appropriate action to mitigate the risk.

![Project Diagram](Diagram/Final_Diagram.jpg)
