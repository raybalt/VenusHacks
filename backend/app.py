from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

# from your_code import really_complex_function

app = Flask(__name__)
CORS(app)

YELP_AUTH_TOKEN = 'kKEL1ma2XlqXPV7sxAwD9zbYi-Jy8_pGNLzaxacWhjxVEFpRFvXu0hFbufUonkNumc0LPangXBiuWt5-cR5A-4TyjDGiCDNffeizvEC3x-gakP8I0gw0WqDs1l5yZHYx'

# Access this endpoint through: http://localhost:5000/
@app.route('/')
def index():
    return jsonify({'message': 'Hey, everything works!!'})

# Access this endpoint through: http://localhost:5000/yelp-test
@app.route('/yelp-test/')
def yelp_default_test():
    
    
    url = "https://api.yelp.com/v3/businesses/search"

    querystring = {"location": "Irvine, CA", "term": "contraceptive"}
    querystring1 = {"location": "Irvine, CA", "term": "abortion"}
    querystring2 = {"location": "Irvine, CA", "term": "IVF"}
    querystring3 = {"location": "Irvine, CA", "term": "menstrual"}
    querystring4 = {"location": "Irvine, CA", "term": "Plan B"}

    headers = {"Authorization": "Bearer " + 'kKEL1ma2XlqXPV7sxAwD9zbYi-Jy8_pGNLzaxacWhjxVEFpRFvXu0hFbufUonkNumc0LPangXBiuWt5-cR5A-4TyjDGiCDNffeizvEC3x-gakP8I0gw0WqDs1l5yZHYx'}

    contra_response = requests.request(
        "GET", url, headers=headers, params=querystring)
    abort_response = requests.request(
        "GET", url, headers=headers, params=querystring1)
    ivf_response = requests.request(
        "GET", url, headers=headers, params=querystring2)
    mens_response = requests.request(
        "GET", url, headers=headers, params=querystring3)
    planb_response = requests.request(
        "GET", url, headers=headers, params=querystring4)

    return jsonify(contra_response.json())
