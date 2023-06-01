import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Load the saved model
model = tf.keras.models.load_model('model.h5')

# Define a function to preprocess the image
def preprocess_image(image):
    # Resize the image to the size expected by the model
    img = image.resize((224, 224))
    # Convert the image to a NumPy array
    img_array = np.array(img)
    # Normalize the pixel values
    img_array = img_array / 255.0
    # Expand the dimensions to match the input shape of the model
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Define a function to make a prediction on a new image
def predict_image(image_path):
    # Load the image from disk
    img = Image.open(image_path)
    # Preprocess the image
    img_array = preprocess_image(img)
    # Make a prediction using the pre-trained model
    predictions = model.predict(img_array)
    # Get the class with the highest predicted probability
    predicted_class = np.argmax(predictions)
    # Return the predicted class label
    return predicted_class

# Test the prediction function on a sample image
image_path = 'test.jpg'
predicted_class = predict_image(image_path)
print(predicted_class)
