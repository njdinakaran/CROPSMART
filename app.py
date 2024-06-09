from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import os
from flask import jsonify
from flask import url_for


from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
from keras.preprocessing import image

from tensorflow.keras.preprocessing.image import load_img

import tensorflow as tf

app = Flask(__name__)
# Define the path to the model file

# defining image directory

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

# designing works starts here
crop_descriptions = {
    "banana.jpg": "Bananas thrive in warm, humid environments, making your climate ideal for their growth. Additionally, the well-drained soil suggested by your NPK levels is optimal for banana cultivation, promoting healthy root development and nutrient uptake.",
    "blackgram.png": "Blackgram is well-suited to warm climates with moderate rainfall, aligning perfectly with your environmental conditions. Its ability to fix nitrogen makes it beneficial for soil health, while its tolerance to drier conditions ensures resilience during periods of reduced rainfall.",
    "chickpea.jpg": "Chickpeas, being nitrogen-fixing legumes, are particularly suited for areas with moderate rainfall. Their ability to thrive in drier conditions makes them resilient to fluctuations in precipitation, while their nitrogen-fixing ability enriches the soil, benefiting future crops.",
    "coconut.png": "Coconut palms thrive in warm, humid climates, making them an excellent fit for your land. Their deep root systems and tolerance to high temperatures ensure their resilience in your environmental conditions, while their moderate water needs align well with your rainfall patterns.",
    "coffee.png": "Coffee plants prefer slightly acidic soil, and your specific pH level suggests an environment conducive to their growth. With the right soil conditions and adequate moisture, coffee plants can thrive in your climate, producing high-quality beans for harvest.",
    "cotton.png": "Cotton thrives in warm temperatures, making your climate ideal for its cultivation. The combination of warm temperatures and the well-drained soil suggested by your data provides optimal conditions for cotton growth, promoting healthy plant development and fiber production.",
    "grapes.png": "Grapes prefer warm temperatures and abundant sunlight, both of which are characteristic of your climate. With the right conditions, including well-drained soil and adequate sunlight, grapevines can flourish on your land, producing high-quality fruit for harvest.",
    "groundnuts.png": "Groundnuts thrive in warm temperatures and are relatively drought tolerant, making them well-suited for your climate. Additionally, their ability to fix nitrogen enriches the soil, benefiting future crops, while their moderate water needs align with your rainfall patterns, reducing irrigation demands.",
    "jute.png": "Jute thrives in warm and humid conditions, which align well with your temperature and humidity levels. Its moderate water needs and tolerance to varying soil conditions make it a suitable crop for your land, potentially reducing irrigation demands and promoting sustainable cultivation practices.",
    "kidneybeans.jpg": "Kidney beans prefer warm climates, as indicated by your temperature data. Additionally, their moderate water needs align with your rainfall patterns, reducing irrigation demands. Their ability to fix nitrogen enriches the soil, benefiting future crops, particularly if nitrogen levels are slightly low.",
    "lentil.png": "Lentils, like other legumes, fix nitrogen from the air and deposit it in the soil, enriching it for future crops. This nitrogen-fixing ability makes lentils beneficial for soil health, while their moderate water needs align with your rainfall patterns, reducing irrigation demands.",
    "maize.jpeg": "Maize has a moderate to high demand for nutrients, and the NPK levels you provided might be favorable for its growth. Additionally, the warm temperatures and well-drained soil suggested by your data align well with maize's preference for good drainage and optimal growing conditions, promoting healthy plant development and yield.",
    "mango.png": "Mangoes thrive in warm climates with well-drained soil, both of which are characteristic of your land. The combination of warm temperatures and optimal soil conditions provides an ideal environment for mango trees to flourish, producing high-quality fruit for harvest.",
    "mothbean.png": "Mothbeans are an ideal choice for your land due to their drought tolerance and ability to grow in a wide range of soil conditions. These characteristics make them resilient to fluctuations in rainfall and soil type, ensuring consistent yields even under variable environmental conditions.",
    "mungbeans.png": "Mungbeans are an excellent choice for your land because they are legumes and thrive in warm conditions. Their ability to fix nitrogen enriches the soil, benefiting future crops, while their moderate water needs align with your rainfall patterns, potentially reducing irrigation demands and promoting sustainable cultivation practices.",
    "muskmelon.png": "Muskmelon's high water content complements moderate rainfall, potentially reducing irrigation needs. Hence, it is the most favorable plant for your land, ensuring optimal fruit development and yield under your environmental conditions.",
    "orange.jpeg": "Oranges have the potential to flourish on your land due to their deep root systems and moderate water needs, which align well with your rainfall patterns. Their ability to access nutrients lower in the soil ensures consistent growth and fruit production, making them an ideal crop for your environmental conditions.",
    "papaya.png": "Papaya thrives in tropical climates and doesn't require excessive water, potentially making it adaptable to your rainfall patterns. Its ability to tolerate a range of soil conditions ensures resilience in varying environmental conditions, promoting sustainable cultivation practices and consistent yields.",
    "pigeonpeas.png": "Pigeonpea is well-suited for your land due to its deep root system, drought tolerance, and nitrogen-fixing ability. These characteristics enable pigeonpeas to access nutrients lower in the soil and enrich it for future crops, while their ability to thrive in warm climates ensures consistent growth and yield under your environmental conditions.",
    "pomegranate.png": "Pomegranate tolerates a range of soil conditions, making it adaptable to your land. The NPK balance and well-drained soil suggested by your data align well with pomegranate's needs, promoting healthy fruit development and yield under your environmental conditions.",
    "rice.jpg": "Rice appears well-suited for your land, thriving in warm, humid conditions with a good water supply. Paddy rice cultivation is a productive choice for your land, potentially ensuring high yields and profitability under your environmental conditions.",
    "watermelon.png": "Watermelon could be a good fit for your land due to warm temperatures, moderate rainfall, and well-drained soil indicated by your NPK levels. These conditions provide an optimal environment for watermelon cultivation, ensuring high-quality fruit development and yield under your environmental conditions."
}

@app.route("/")
def Display_IMG():
    IMG_LIST = os.listdir("static/img")
    IMG_LIST = ["img/" + i for i in IMG_LIST]
    return render_template("crop_predict.html", imagelist=IMG_LIST, static_url_path=app.static_url_path)

if __name__ == "__main__":
    app.run(debug=True)