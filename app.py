import io
import json
import torch
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request

import import_ipynb
from CNN_Inference import Image_Prediction, Video_Prediction
from Model_Utils import classes, transform_PIL, model

app = Flask(__name__)

# Define your custom transform
def custom_transform(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    return transform_PIL(image).unsqueeze(0)

# Load your model from the checkpoint (modify the path accordingly)
checkpoint_path = 'Best_Checkpoint.model'
model.load_state_dict(torch.load(checkpoint_path))
model.eval()

def get_prediction(image_bytes):
    tensor = custom_transform(image_bytes=image_bytes)
    outputs = model(tensor)
    _, predicted = torch.max(outputs, 1)
    class_name = predicted
    return class_name

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            img_bytes = file.read()
            class_name = get_prediction(image_bytes=img_bytes)
            return jsonify({'prediction': class_name})
        else:
            return jsonify({'error': 'No file part'})

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Image Prediction API.'

if __name__ == '__main__':
    app.run()
