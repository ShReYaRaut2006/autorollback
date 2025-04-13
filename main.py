from flask import Flask
import os

app = Flask(__name__)  

@app.route('/')
def hello():
    return "🚀 Hello from version this is new update! successful this the version 1"

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=8000)

