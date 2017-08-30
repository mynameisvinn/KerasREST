import numpy as np

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD

def create_model(X, y):
    model = Sequential()
    model.add(Dense(8, input_dim=2))
    model.add(Activation('relu'))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))
    sgd = SGD(lr=0.01)
    model.compile(loss='binary_crossentropy', optimizer=sgd)
    model.fit(X, y, batch_size=1, epochs=1000, verbose=0)
    return model

if __name__ == '__main__':
    X = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")
    y = np.array([[0],[1],[1],[0]], "float32")

    m = create_model(X, y)
    m.save("models/xor.h5")

    print "input data: ", X
    print "predictions: ", m.predict(X)
    print "predictions: ", m.predict_classes(X)