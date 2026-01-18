from flask import Flask

app = Flask(__name__)

@app.get("/home")
def home():
    return "Hello World Vadias"

app.run(debug=True)   
