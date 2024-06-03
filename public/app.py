from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
# Define the path to the model file
model_path = 'crop.pkl'

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/crop_predict')
def crop_predict():
    city = request.args.get('city')
    return render_template('crop_predict.html', city=city)


if __name__ == "__main__":
    app.run(debug=True)