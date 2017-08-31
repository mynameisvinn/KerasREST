import os
from flask import Flask, jsonify, request, abort
from keras.models import load_model

app = Flask(__name__)
model = load_model("models/xor.h5")

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/api', methods=['GET'])
def get_tasks():
    return jsonify({'n_layers': len(model.layers)})

# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
@app.route('/api', methods=['PUT'])
def predict():
    if not request.json or not 'input' in request.json:
        abort(400)
    else:
        predictions = model.predict(request.json['input']).tolist()
        return jsonify({"pred_val": predictions})

if __name__ == '__main__':
    app.run(
    	host=os.getenv('LISTEN', '0.0.0.0'),
    	port=int(os.getenv('PORT', '5000'))
    	)