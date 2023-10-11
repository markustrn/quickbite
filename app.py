from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = 'AIzaSyAMgkgsxUqUtt16XJzcUPc0EUA-c_P8mUI'

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
