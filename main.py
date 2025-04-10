from flask import Flask
import os

app = Flask(_name_)

# Read and increment version
version_file = "version.txt"

with open(version_file, "r") as f:
    version = f.read().strip() 
 
# Try to convert and increment version
try:
    version_num = int(version)
    new_version = version_num + 1
except ValueError:
    new_version = version  # fallback if version is not a number

# Write updated version back to file
with open(version_file, "w") as f:
    f.write(str(new_version))

@app.route('/')
def hello():
    return f"🚀 Hello from version this is new update! successful this the version 4"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8000)
  
