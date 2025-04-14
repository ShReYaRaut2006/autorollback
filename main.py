from flask import Flask
import os

app = Flask(_name_)  

@app.route('/')
def hello():
    return "🚀 Hello world "

if _name_ == '_main_': 
    app.run(host='0.0.0.0', port=8000)
