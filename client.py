import requests

def make_prediction(X_test):
    """
    send PUT request to an IP:PORT. a server should be listening 
    on the other end, ready to respond with predictions.
    """
    # r = requests.put("http://ec2-54-67-101-240.us-west-1.compute.amazonaws.com:5000/api", json={'input': X_test})
    r = requests.put("http://localhost:5000/api", json={'input': X_test})
    # r = requests.put("http://192.168.99.100:5000/api", json={'input': X_test})
    return r.json()['pred_val']

if __name__ == '__main__':

    # test data
    X_inputs = [[1, 1], [0, 1]]
    pred = make_prediction(X_inputs)
    for i in zip(X_inputs, pred):
        print(i)