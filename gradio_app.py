import gradio as gr
import tensorflow as tf
import numpy as np
import cv2
from model_utils import preprocess_image, EMNIST_LABELS

# Load model
model = tf.keras.models.load_model('model_emnist.h5')

def predict(img):
    if img is None:
        return "Silakan masukkan gambar"
    
    # Preprocess
    processed = preprocess_image(img)
    
    # Prediksi
    prediction = model.predict(processed)
    index = np.argmax(prediction)
    conf = np.max(prediction) * 100
    
    char = EMNIST_LABELS[index]
    return f"Hasil: {char} (Keyakinan: {conf:.2f}%)"

# Tampilan Gradio
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(),
    outputs="text",
    title="Sistem Deteksi Tulisan Tangan CNN (DINAR FADILAH)"
)

if __name__ == "__main__":
    demo.launch(share=True)