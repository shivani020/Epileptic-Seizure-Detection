# epileptic-seizure-detection

 <p align="center">
  <img src="https://img.icons8.com/ios-filled/100/brain.png" width="80" />
  <h1 align="center">Epileptic Seizure Detection</h1>
  <p align="center">A CNN-powered app to detect seizures from EEG signals</p>
  <p align="center">
    <img src="https://img.shields.io/badge/Made%20with-❤️%20by%20Shivani-blue?style=flat-square" />
  </p>
</p>

---

## Project Overview

A deep learning-based web application that analyzes EEG signals and detects if a person is experiencing a seizure using a Convolutional Neural Network (CNN). Built with Flask and designed for real-world deployment.

---

## Features

-  CNN-based classification of EEG signals
-  Real-time EEG signal visualization
-  Prediction confidence score
-  Elegant UI using Bootstrap
-  Secure `.env` config
-  Cloud-deployable (Render ready!)

---

## How to Run Locally

```bash
# Clone repository
git clone https://github.com/yourusername/Epileptic-Seizure-Detection.git
cd Epileptic-Seizure-Detection

# Set up environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt


# Add environment variables
cp .env.example .env

# Run the Flask server
python app.py

---

# Screenshots
![ss2](https://github.com/user-attachments/assets/76badc45-563b-4c0b-865e-f3f4f049bd30)

![ss1](https://github.com/user-attachments/assets/f999e322-f163-4838-9a6d-3d2f24fad0b3)

---

# Sample Prediction Output
EEG ID: Sample_2

Actual Label: 3 (seizure)

Prediction: Seizure

Confidence: 91.45%

---


# Tech Stack

       Layer             Tech              
| ------------- | ----------------- |
| ML Model      | TensorFlow, Keras |
| Web Framework | Flask             |
| UI Framework  | Bootstrap 5       |
| Data Handling | Pandas, NumPy     |
| Plotting      | Matplotlib        |
| Deployment    | Render / Gunicorn |


---


#  📁 Project Structure

├── app.py
├── train_model.py
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   ├── plot.png
├── model/
│   └── seizure_model.h5
├── uploads/
|     └──eeg_data.csv
├── .env
├── .gitignore
├── requirements.txt
└── README.md


---


# 👨‍💻 Contributors

Shivani – Developer & ML Engineer

shivani030303@gmail.com


---


# 🙏 Acknowledgements

Open EEG dataset contributors

Professors & mentors for guidance

OpenAI & GitHub Copilot for coding assistance



