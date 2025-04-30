from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = os.uname()[1] # Get container hostname
    return f"<h1>Hello from my DevOps Lab!</h1><p>Running on container: {hostname}</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)