from flask import Flask
import os

app = Flask(___name___)  

@app.route('/')
def hello():
    return "🚀 Hello world "

if ___name___ == '___main___': 
    app.run(host='0.0.0.0',port=8000)
