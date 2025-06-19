import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# Class labels (same order as training)
class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# Load your trained model
model = tf.keras.models.load_model("garbage_model.h5")

# Prediction function
def predict_image(img):
    img = img.resize((124, 124))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)[0]
    return {class_names[i]: float(predictions[i]) for i in range(len(class_names))}

# Gradio interface
interface = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3),
    title="🗑️ Garbage Classifier with EfficientNet",
    description="Upload a garbage image to predict its type: plastic, paper, metal, etc."
)

interface.launch()

