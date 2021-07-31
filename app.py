from flask import  Flask, request, render_template
import os
import pickle
import zipfile

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	message = "HELLO WORLD"
	return message

if __name__ == '__main__':
	app.run(debug=True)
