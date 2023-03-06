# To run flask app: Follow the below steps

#  > set FLASK_APP=hello.py
#  > set FLASK_ENV=development
#  > flask run

# Name app.py as index file
from flask import Flask
app = Flask(__name__)

# Decorator for app route
@app.route("/server", methods=['GET'])
def fetch_server():
    return "<h2>Server Connected</h2>"

@app.route("/connected", methods=['GET'])
def set_connected():
    return "Connected"

@app.route("/", methods=['GET'])
def home():
    return fetch_server()
    # return set_connected()

if __name__ == "__main__":
    app.run(debug=True)



