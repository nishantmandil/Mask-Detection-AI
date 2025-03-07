Mask Detection using OpenCV

This project detects whether a person is wearing a mask or not using Haar cascades in OpenCV. The program captures live video from the webcam, detects faces, and classifies them as either "Mask Detected" or "No Mask" using a pre-trained XML classifier.

Features

Detects faces using haarcascade_frontalface_default.xml

Classifies faces as "Mask Detected" or "No Mask" using mask.xml

Draws bounding boxes with color-coded labels:

✅ Green: Mask detected 😷

❌ Red: No mask ❌

Real-time webcam support

Simple and lightweight implementation

Installation

Prerequisites

Python 3.7+

OpenCV

Webcam

Setup

Clone the repository:

git clone https://github.com/yourusername/mask-detection-opencv.git
cd mask-detection-opencv

Install dependencies:

pip install opencv-python

Ensure the required Haar cascade files are present:

haarcascade_frontalface_default.xml

mask.xml

Usage

Run the script to start the real-time mask detection:

python mask_detection.py

How It Works

The script captures frames from the webcam.

It converts each frame to grayscale.

It detects faces using the haarcascade_frontalface_default.xml.

It then applies mask.xml to classify whether the person is wearing a mask.

The output is displayed with a bounding box and label.

Press q to exit the program.

Known Issues

Haar cascades are not always accurate for mask detection.

For better accuracy, consider using a deep learning model like MobileNetV2 or OpenCV DNN.

Future Improvements

Implement deep learning-based mask detection using TensorFlow/Keras.

Add support for video files instead of just live webcam.

Improve mask classifier accuracy with a larger dataset.

Contributing

Feel free to open issues or contribute to improving this project. Fork, make your changes, and submit a pull request!
