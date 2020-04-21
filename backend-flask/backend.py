from flask import Flask, request, jsonify,render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)    

@app.route("/test")
def test():
    return "Hello!! Yoy are connected!\n"    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
