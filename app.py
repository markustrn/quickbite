from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


app = Flask(__name__)



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
gi