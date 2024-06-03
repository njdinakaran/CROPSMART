from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd


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
    











if __name__ == "__main__":
    app.run(debug=True)