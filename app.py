from flask import Flask, request, render_template
from PIL import Image
from tensorflow import keras
import numpy as np
from keras.preprocessing import image
import os
os.environ["CUDA_VISIBLE_DEVICES"] = '-1'
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

app = Flask(__name__)
# Loading model

loaded_model = keras.models.load_model("model2")


@app.route('/', methods=['GET', 'POST'])
def home():
    message = "HELLO WORLD"
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # Read in image from request
    rawImage = request.files["image"]
    # Open image using PIL
    imageData = Image.open(rawImage)
    # Resize image to match size used during training
    imageData = imageData.resize((180, 180))
    # Does something related to dims
    new_image = np.expand_dims(image.img_to_array(imageData), axis=0)
    # Push it into the predict model
    result = loaded_model.predict(new_image)
    print(result)
    if result[0][0] > 0:
        return "Hot Dog"
    else:
        return "Not Hot Dog"


if __name__ == '__main__':
    app.run(debug=True)
