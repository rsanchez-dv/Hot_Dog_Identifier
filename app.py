from flask import  Flask, request, render_template
import os
import pickle
import zipfile

app = Flask(__name__)
# Loading model

@app.route('/', methods=['GET', 'POST'])
def home():
	message = "HELLO WORLD"
	return message

@app.route('/predict', methods=['GET','POST'])
def predict():
	return "Not Hotdog"

if __name__ == '__main__':
	app.run(debug=True)
