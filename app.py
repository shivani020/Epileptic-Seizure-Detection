from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
import os

load_dotenv()

model_path = os.getenv("MODEL_PATH", "model/seizure_model.h5")
model = tf.keras.models.load_model(model_path)


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Load model
model = tf.keras.models.load_model('model/seizure_model.h5')

# Load data
data = pd.read_csv('uploads/eeg_data.csv')
feature_columns = data.columns[1:-1]  # Ignore ID and label
label_column = 'y'

# Encode original labels for inverse_transform
le = LabelEncoder()
le.fit(data[label_column].values)

@app.route('/')
def index():
    # Randomly select 5 samples
    samples = data.sample(5).reset_index(drop=True)
    sample_ids = samples.iloc[:, 0].tolist()  # ID column
    return render_template('index.html', samples=samples, sample_ids=sample_ids)

@app.route('/predict', methods=['POST'])
def predict():
    selected_index = int(request.form['sample_index'])
    sample = data.iloc[selected_index]
    sample_id = sample.iloc[0]
    actual_label = sample[label_column]

    # Extract features
    features = sample[1:-1].astype(float).values.reshape(1, -1, 1)

    # Predict
    probabilities = model.predict(features)[0]  # Probabilities for all classes
    predicted_class = np.argmax(probabilities)
    predicted_label = le.inverse_transform([predicted_class])[0]
    confidence = np.max(probabilities) * 100

    # EEG plot
    fig, ax = plt.subplots()
    ax.plot(sample[1:-1].astype(float).values)
    ax.set_title(f'EEG Sample: {sample_id}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    plot_path = os.path.join('static', 'plot.png')
    fig.savefig(plot_path)
    plt.close()

    return render_template('result.html',
                           sample_id=sample_id,
                           actual_label=actual_label,
                           predicted_label=predicted_label,
                           confidence=round(confidence, 2),
                           plot_url=plot_path)

if __name__ == '__main__':
    app.run(debug=True)
