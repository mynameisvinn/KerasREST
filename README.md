# keras server
deploying keras model through rest.

## training the model
run `python train.py` to train a XOR model. we'll keep it simple and use a binary classifier with a 1 single hidden layer.

## deploying
### option 1: local
assuming a trained model exists, run:
```bash
python server.py
python client.py  # separate terminal
```

### option 2: docker
first, build docker image with `docker build -t mynameisvinn/kerasrest .` (dont forget the period).

then, run docker with `docker run -d -p 5000:5000 mynameisvinn/kerasrest`. the argument `-p 5000:5000` binds the container's port to local port.

finally, from another terminal, run `python client.py`. remember, docker containers are *virtual machines* and therefore have unique ip addresses; youll need your container's ip, which can be found by `docker-machine ip default`. 

### option 3: ec2
#### spin up ec2 and provision
use an existing image `ami-125b2c72` (in the us-west-1 region). this image contains caffe, torch, theano, keras and lasagne. [more information](http://cs231n.github.io/aws-tutorial/).

youll need the latest version of keras:
```bash
pip install git+git://github.com/fchollet/keras.git --upgrade --no-deps
```

since we'll be remotely calling this instance, we'll need to update security policy such that port 5000 is open to all incoming traffic.

finally, ssh into this instance, clone this repo, and run:
```bash
git clone https://github.com/mynameisvinn/KerasREST
cd KerasREST
python server.py
```

#### client rest calls
from your local machine, run `python client.py`. make sure it points to the correct ec2 instance (eg http://ec2-54-67-101-240.us-west-1.compute.amazonaws.com:5000/api) and not `localhost`.

for example:
```python
def make_prediction(X_test):
    r = requests.put("http://ec2-54-67-101-240.us-west-1.compute.amazonaws.com:5000/api", json={'input': X_test})  # point to your ec2 dns
    resp = r.json()['pred_val']
    return resp
```
