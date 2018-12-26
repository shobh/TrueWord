#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for
#from flask_heroku import Heroku
import os, json, yaml
app = Flask(__name__)
#heroku = Heroku(app)



SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, 'data.json')
data = json.load(open(json_url, encoding="utf-8"))



@app.route('/')
def index():
    return "True Words"

@app.route('/api/types', methods=['GET'])
def get_types():
    return "1"
	
@app.route('/api/quote', methods=['GET'])
def get_quote():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

