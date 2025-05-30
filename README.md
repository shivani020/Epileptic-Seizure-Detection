# epileptic-seizure-detection

 <p align="center">
  <img src="https://img.icons8.com/ios-filled/100/brain.png" width="80" />
  <h1 align="center">Epileptic Seizure Detection</h1>
  <p align="center">A CNN-powered app to detect seizures from EEG signals</p>
  <p align="center">
    <img src="https://img.shields.io/badge/Status-Production-green?style=flat-square" />
    <img src="https://img.shields.io/github/stars/shivani020/Epileptic-Seizure-Detection?style=flat-square" />
    <img src="https://img.shields.io/github/forks/shivani020/Epileptic-Seizure-Detection?style=flat-square" />
    <img src="https://img.shields.io/badge/Made%20with-❤️%20by%20Shivani-blue?style=flat-square" />
  </p>
</p>

---

## 🧠 Project Overview

A deep learning-based web application that analyzes EEG signals and detects if a person is experiencing a seizure using a Convolutional Neural Network (CNN). Built with Flask and designed for real-world deployment.

---

## 💡 Features

- 🧠 CNN-based classification of EEG signals
- 📊 Real-time EEG signal visualization
- 🎯 Prediction confidence score
- 🌐 Elegant UI using Bootstrap
- 🔐 Secure `.env` config
- ☁️ Cloud-deployable (Render ready!)

---

## ⚙️ How to Run Locally

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

