import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, MaxPooling1D, Flatten, Dropout, BatchNormalization
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load CSV file
file_path = 'uploads/eeg_data.csv'  # apna csv file path daalo

# Load data with header
df = pd.read_csv(file_path, header=0)

# Drop first column (ID) and last column (label) from features
df_features = df.drop([df.columns[0], 'y'], axis=1)

# Convert features to float numpy array
X = df_features.astype(float).values

# Labels
y_raw = df['y'].values

# Encode labels to integers
le = LabelEncoder()
y = le.fit_transform(y_raw)

# Number of classes (0-4)
num_classes = len(np.unique(y))

# One-hot encode labels for multi-class classification
y_cat = to_categorical(y, num_classes)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_cat, test_size=0.2, random_state=42)

# Reshape for Conv1D: (samples, timesteps, channels)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# Model definition
model = Sequential([
    Conv1D(64, kernel_size=3, activation='relu', input_shape=(X_train.shape[1], 1)),
    BatchNormalization(),
    MaxPooling1D(pool_size=2),
    Dropout(0.25),

    Conv1D(128, kernel_size=3, activation='relu'),
    BatchNormalization(),
    MaxPooling1D(pool_size=2),
    Dropout(0.25),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.1)

# Save the model
model.save('model/seizure_model.h5')
