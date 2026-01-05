import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import os
import zipfile

def load_emnist_data():
    print("📥 Mengakses dataset")
    from emnist import extract_training_samples, extract_test_samples
    
    # Memastikan file ada sebelum ekstrak
    cache_path = '/root/.cache/emnist/emnist.zip'
    if not os.path.exists(cache_path):
        raise FileNotFoundError("File emnist.zip tidak ditemukan")

    # Load data (balanced)
    x_train, y_train = extract_training_samples('balanced')
    x_test, y_test = extract_test_samples('balanced')

    # Preprocessing
    x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
    x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0
    
    return (x_train, y_train), (x_test, y_test)

def run_training():
    (x_train, y_train), (x_test, y_test) = load_emnist_data()
    
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(47, activation='softmax') # 47 kelas untuk 'balanced'
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    print("Memulai Training...")
    # Pakai 10 epoch saja dulu agar cepat buat ngetes
    model.fit(x_train, y_train, epochs=10, batch_size=128, validation_data=(x_test, y_test))
    
    model.save('model_emnist.h5')
    print("MODEL BERHASIL disimpan sebagai 'model_emnist.h5'")

if __name__ == "__main__":
    run_training()