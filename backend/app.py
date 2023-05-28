from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

# from your_code import really_complex_function

app = Flask(__name__)
CORS(app)

YELP_AUTH_TOKEN = 'Wbtvkn5ry53fhvW7q0eZiugyedp1rhbKNywEqANTOFo9zQCokmiXygNsDVSWSbrYEj8tqxEopf9GjxfC1H0xRZNPFNq1RsApFR74HLQVxpHbw8DBevoxo_2_pDZzZHYx'

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

    headers = {"Authorization": "Bearer " + 'Wbtvkn5ry53fhvW7q0eZiugyedp1rhbKNywEqANTOFo9zQCokmiXygNsDVSWSbrYEj8tqxEopf9GjxfC1H0xRZNPFNq1RsApFR74HLQVxpHbw8DBevoxo_2_pDZzZHYx'}

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return jsonify(response.json())
