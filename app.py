from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd

from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
from keras.preprocessing import image

from tensorflow.keras.preprocessing.image import load_img

import tensorflow as tf

app = Flask(__name__)
# Define the path to the model file

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/crop_predict')
def crop_predict():
    city = request.args.get('city')
    return render_template('crop_predict.html', city=city)


@app.route('/index')
def index_move():
    city = request.args.get('city')
    return render_template('index.html', city=city)

@app.route('/pest_predict')
def pest_predict():
    return render_template('pest_predict.html')

@app.route('/weed_predict')
def weed_predict():
    return render_template('weed_predict.html')

# page movement end

#crop prediction model 
model = pickle.load(open('crop.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['nitrogen']
    data2 = request.form['phosphorus']
    data3 = request.form['potassium']
    data4 = request.form['temperature']
    data5 = request.form['humidity']
    data6 = request.form['ph']
    data7 = request.form['rainfall']
    
    # Define feature names
    feature_names = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
# Create NumPy array with feature names
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7]])

# Set feature names
    arr = pd.DataFrame(arr, columns=feature_names)
    pred = model.predict(arr)
    print(pred)
    return render_template('crop_result.html', data=pred)


#weed model
weedmodel = load_model('weed_model.h5')
weedmodel.make_predict_function()

def predict_label(img_path):
    img = Image.open(img_path)
    img = img.resize((224, 224))  # Resize the image to the required size
    img_array = np.array(img) / 255.0  # Convert image to numpy array and normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    p = np.argmax(weedmodel.predict(img_array), axis=1)
    return p

WEED_NAMES = {
    0: "Amaranthus spp",
    1: "Chenopodium album",
    2: "Cirsium arvense",
    3: "Commelina benghalensis",
    4: "Convolvulus arvensis",
    5: "Cyperus rotundus",
    6: "Dactyloctenium aegyptium",
    7: "Echinochloa crus-galli",
    8: "Parthenium hysterophorus",
    9: "Phalaris minor"
}

@app.route("/submit", methods=['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']

        img_path = "static/" + img.filename
        img.save(img_path)

        p = predict_label(img_path)
        weed_name = WEED_NAMES.get(p[0], "Unknown Weed")

    return render_template("weed_result.html", data=p, weed_name=weed_name, img_path=img_path)


# pest identification===================================

model_path = 'pest_ince.tflite'
# Load the TFLite model and allocate tensors
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Function to preprocess the image
def preprocess_image(image_path, target_size=(224, 224)):
    img = Image.open(image_path)
    img = img.resize(target_size)
    img = np.array(img) / 255.0  # Normalize to [0, 1]
    img = img.astype(np.float32)  # Convert to FLOAT32
    img = np.expand_dims(img, axis=0)
    interpreter.set_tensor(input_details[0]['index'], img)
        # Run the model
    interpreter.invoke()
    # Get the predicted class
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_class = np.argmax(output_data)

    return predicted_class

PEST_NAMES = {
    0: "Anoplophora chinensis",
    1: "Apriona germari hope",
    2: "Cerambycidae larvae",
    3: "Chalcophora japonica",
    4: "Clostera anachoreta",
    5: "Cnidocampa flavescens Walker pupa",
    6: "Cnidocampa flavescens walker",
    7: "Drosicha contrahens female",
    8: "Drosicha contrahens male",
    9: "Erthesina fullo",
    10: "Erthesina fullo nymph",
    11: "Erthesina fullo nymph-2",
    12: "Hyphantria cunea",
    13: "Hyphantria cunea larvae",
    14: "Hyphantria cunea pupa",
    15: "Latoia consocia Walker",
    16: "Latoia consocia Walker larvae",
    17: "Micromelalopha troglodyta Graeser",
    18: "Micromelalopha troglodyta Graeser larvae",
    19: "Monochamus alternatus",
    20: "Plagiodera versicolora Laicharting",
    21: "Plagiodera versicolora Laicharting larvae",
    22: "Plagiodera versicolora Laicharting ovum",
    23: "Psacothea hilaris Pascoe",
    24: "Psilogramma menephron",
    25: "Psilogramma menephron larvae",
    26: "Sericinus montela",
    27: "Sericinus montela larvae",
    28: "Spilarctia subcarnea Walker",
    29: "Spilarctia subcarnea Walker larvae",
    30: "Spilarctia subcarnea Walker larvae-2"
}

@app.route("/pestsubmit", methods=['GET', 'POST'])
def get_prediction():
    if request.method == 'POST':
        img = request.files['my_image']

        img_path = "static/" + img.filename
        img.save(img_path)

        p = preprocess_image(img_path)
        pest_name = PEST_NAMES.get(p, "Unknown Pest")

    return render_template("pest_result.html", data=p, pest_name=pest_name, img_path=img_path)

if __name__ == "__main__":
    app.run(debug=True)