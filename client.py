import requests

def make_prediction(X_test):
    # r = requests.put("http://ec2-54-67-101-240.us-west-1.compute.amazonaws.com:5000/api", json={'input': X_test})
    r = requests.put("http://localhost:5000/api", json={'input': X_test})
    resp = r.json()['pred_val']
    return resp

def nb_layers():
    response = requests.get("http://localhost:5000/api")
    return response.content

if __name__ == '__main__':
    X_inputs = [[1, 1], [0, 1]]
    pred = make_prediction(X_inputs)
    for i in zip(X_inputs, pred):
        print i