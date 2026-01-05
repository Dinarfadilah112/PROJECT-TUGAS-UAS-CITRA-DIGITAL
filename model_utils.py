import numpy as np
import cv2

# Label EMNIST Balanced (47 kelas)
EMNIST_LABELS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'd', 'e', 'f', 'g', 'h', 'n', 'q', 'r', 't'
]

def get_class_labels():
    return EMNIST_LABELS

def preprocess_image(img_numpy):
    """
    Fungsi preprocessing untuk foto dari HP:
    Grayscale -> Threshold -> Resize 28x28
    """
    # 1. Grayscale
    if len(img_numpy.shape) == 3:
        gray = cv2.cvtColor(img_numpy, cv2.COLOR_BGR2GRAY)
    else:
        gray = img_numpy

    # 2. Thresholding (Membuat tulisan jadi putih, background hitam)
    # Otsu's thresholding agar adaptif dengan cahaya foto
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # 3. Resize ke 28x28
    resized = cv2.resize(thresh, (28, 28), interpolation=cv2.INTER_AREA)
    
    # 4. Normalisasi
    img_final = resized.reshape(1, 28, 28, 1).astype('float32') / 255.0
    
    return img_final