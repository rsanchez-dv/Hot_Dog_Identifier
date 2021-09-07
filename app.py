from flask import  Flask, request, render_template
import os
import pickle
import zipfile

app = Flask(__name__)
# Loading model

@app.route('/', methods=['GET', 'POST'])
def home():
	message = "HELLO WORLD"
	return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
	print(request.data)
	return "RESPONSE"
if __name__ == '__main__':
	app.run(debug=True)
