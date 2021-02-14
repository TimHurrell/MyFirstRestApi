from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello'

@app.route('/myendpoint/', methods=['GET'])
def getworld():
  return jsonify ('Hello World!')