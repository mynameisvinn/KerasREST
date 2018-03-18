import numpy as np

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD

def build_model(X, y):
    model = Sequential()
    model.add(Dense(8, input_dim=2))
    model.add(Activation('relu'))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer=SGD(lr=0.01))
    model.fit(X, y, batch_size=1, epochs=1000, verbose=0)
    return model

if __name__ == '__main__':
    # generate data
    X = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")
    y = np.array([[0],[1],[1],[0]], "float32")

    # train and save model
    xor_model = build_model(X, y)
    xor_model.save("models/xor.h5")

    # verify answers
    print("input data: ", X)
    print("predictions: ", xor_model.predict(X))
    print("predictions: ", xor_model.predict_classes(X))