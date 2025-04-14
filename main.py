from flask import Flask
import os

app = Flask(_name_)  

@app.route('/')
def hello():
    return "🚀 Hello from version this is new update! successful this the version 1"

if _name_ == '_main_': 
    app.run(host='0.0.0.0', port=8000)
