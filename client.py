from flask import request

def make_prediction(X_test):
    r = requests.put("http://localhost:5000/api", json={'input': X_test})
    resp = r.json()['pred_val']
    return resp

def nb_layers():
    response = requests.get("http://localhost:5000/api")
    return response.content

if __name__ == '__main__':
    X_inputs = [[1, 1], [0, 1]]
    for i in zip(X_inputs, pred):
        print i