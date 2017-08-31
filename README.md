# KerasREST
bare bones example of deploying keras model through REST.

## option 1: usage (localhost)
### 1a: train model
use `python train.py` to train a simple neural network to classify XOR.

### 1b: server
do `python server.py` to serve model locally.

### 1c: client
do `python client.py` to call api.

## option 2: usage (docker)
### 2a: build docker image
build docker image with `docker build -t mynameisvinn/kerasrest .` (dont forget the period).

### 2b: run docker
run docker in detached mode with `docker run -d -p 5000:5000 mynameisvinn/kerasrest`. 

note that `-p 5000:5000` is critical to bind container port to your local machine.

### 2c: client
from local machine, do `python client.py`. youll need to use your docker's container IP, which can be found by `docker-machine ip default`.

## option 3: usage (remote ec2)
### 3a: spin up ec2
use an existing image `ami-125b2c72` (in the us-west-1 region). this image contains caffe, torch, theano, keras and lasagne. [more information](http://cs231n.github.io/aws-tutorial/).

### 3b: update keras
get the latest version of keras with:
```bash
pip install git+git://github.com/fchollet/keras.git --upgrade --no-deps
```
### 3c: update security
for your ec2 instance, update security policy such that
tcp is enabled for all incoming traffic for port 5000.

### 3d: install
get da latest
```bash
git clone https://github.com/mynameisvinn/KerasREST
```
### 3e: server
```bash
cd KerasREST
python server.py
```

### 3f: client
from your local machine, do `python client.py`. 

make sure it points to the correct ec2 instance (eg http://ec2-54-67-101-240.us-west-1.compute.amazonaws.com:5000/api) and not `localhost`.

for example:
```python
def make_prediction(X_test):
    r = requests.put("http://ec2-54-67-101-240.us-west-1.compute.amazonaws.com:5000/api", json={'input': X_test})  # point to your ec2 dns
    resp = r.json()['pred_val']
    return resp
```
