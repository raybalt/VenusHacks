from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

# from your_code import really_complex_function

app = Flask(__name__)
CORS(app)

YELP_AUTH_TOKEN = 'm61qjCN2788Vu6i8a1HjzFOU_Yy-lAJ_Wfh5Y8sl81yzMjHJRDBZS8-BUd21u2Dz2sI9qU6J8j7CopHi9E3wRN-gUnbw1QABXwLoORLuPqQx9S6QFfEE08K_kCBzZHYx'

# Access this endpoint through: http://localhost:5000/
@app.route('/')
def index():
    return jsonify({'message': 'Hey, everything works!!'})

# Access this endpoint through: http://localhost:5000/yelp-test
@app.route('/yelp-test/')
def yelp_default_test():
    
    termtouse = request.args.get('term')
    
    url = "https://api.yelp.com/v3/businesses/search"

    querystring = {"location": "Irvine, CA", "term": termtouse}

    headers = {"Authorization": "Bearer " + 'm61qjCN2788Vu6i8a1HjzFOU_Yy-lAJ_Wfh5Y8sl81yzMjHJRDBZS8-BUd21u2Dz2sI9qU6J8j7CopHi9E3wRN-gUnbw1QABXwLoORLuPqQx9S6QFfEE08K_kCBzZHYx'}

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return jsonify(response.json())
