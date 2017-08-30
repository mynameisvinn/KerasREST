# KerasREST
bare bones example of deploying keras model through REST.

# usage (localhost)
### train model
use `python train.py` to train a simple neural network to classify XOR.

### server
do `python server.py` to serve model over localhost.

### client
do `python client.py` to call api.

## usage (ec2)
### spin up ec2
use an existing image `ami-125b2c72` (in the us-west-1 region). this image contains caffe, torch, theano, keras and lasagne. [more information](http://cs231n.github.io/aws-tutorial/).

### update keras
get the latest version of keras with:
```bash
pip install git+git://github.com/fchollet/keras.git --upgrade --no-deps
```

### update security
for your ec2 instance, update security policy such that
tcp is enabled for all incoming traffic for port 5000.

### server
do `python server.py`

### client
from your local machine, do `python client.py`. make sure it points to the correct ec2 instance (eg http://ec2-54-67-101-240.us-west-1.compute.amazonaws.com:5000/api) and not `localhost`.