#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for
#from flask_heroku import Heroku
import os, json, yaml
app = Flask(__name__)
#heroku = Heroku(app)



SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, 'buddha-quotes.json')
data = json.load(open(json_url, encoding="latin-1"))

json_url2 = os.path.join(SITE_ROOT, 'marcus-aurelius-quotes.json')
data2 = json.load(open(json_url2, encoding="latin-1"))



@app.route('/')
def index():
    return "True Words"

@app.route('/api/types', methods=['GET'])
def get_types():
    return "2"
	
@app.route('/api/quote', methods=['GET'])
def get_quote():
    return jsonify(data)
	
@app.route('/api/quote2', methods=['GET'])
def get_quote2():
    return jsonify(data2)


if __name__ == '__main__':
    app.run(debug=True)

