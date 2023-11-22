import numpy as np
from PIL import Image
from keras.models import load_model
import matplotlib.pyplot as plt
from flask import flash


def Predict(filename):
    classes = ['Actinic keratoses', 'Basal cell carcinoma', 
               'Benign keratosis-like lesions', 'Dermatofibroma', 'Melanoma', 
               'Melanocytic nevi', 'Vascular lesions']
    
    model = load_model("models\HAM10000.h5")

    SIZE = 64
    img_path = 'static/images/'+filename
    # x = plt.imread(Image.open(img_path))
    # plt.imshow(x)
    # plt.show()
    img = Image.open(img_path).resize((SIZE, SIZE))
    img_array = np.array(img)  # Convert image to NumPy array
    img_array = img_array / 255.0  # Normalize pixel values to [0, 1] (assuming 8-bit images)
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    #print(predictions)
    class_idx = np.argmax(predictions)
    print("Diagnosis is: ", classes[class_idx])
    return predictions, classes[class_idx]