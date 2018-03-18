import os
from flask import Flask, jsonify, request, abort
from keras.models import load_model

app = Flask(__name__)
model = load_model("models/xor.h5")

@app.route('/')
def landing():
    """
    default action for localhost:5000

    # https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
    """
    return "hello world!"

@app.route('/api', methods=['GET'])
def get_nlayers():
    """
    response when a GET request is sent to localhost:5000/api.

    returns a json object specifying number of layers in xor model.
    """
    return jsonify({'n_layers': len(model.layers)})


@app.route('/api', methods=['PUT'])
def predict():
    """
    response when a PUT request is sent to localhost:5000/api.
    """
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