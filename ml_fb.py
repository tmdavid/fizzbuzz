from keras.layers import recurrent
from keras.models import Sequential, slice_X
from keras.layers.core import Activation, TimeDistributedDense, RepeatVector, Merge, Dense, Dropout, Flatten, Reshape
from keras.callbacks import EarlyStopping

import numpy as np
import sys

def prepare_data(lines, dim=100000):
    X = []
    Y = []
    for line in lines:
        fizzbuzz = False
        x_np = np.zeros(dim)
        y_np = np.zeros(dim)
        x_y = line.split(" ")
        x = x_y[0]
        y = x_y[1]
        x_np[int(x)]=1
        if 'f' in y:
            y_np[dim-2]=1
            fizzbuzz = True
        if 'b' in y:
            y_np[dim-1]=1
            fizzbuzz = True
        if fizzbuzz is False:
            y_np[int(y)]=1
        X.append(x_np)
        Y.append(y_np)
    return np.asarray(X), np.asarray(Y)

if len(sys.argv)<2:
    raise ValueError('Not specified number of epochs')
else:
    nb_epochs = int(sys.argv[1])
    stacked_layers = 1
    if len(sys.argv)==3:
        stacked_layers = int(sys.argv[2])



inner_layer = 200

lines = [line.rstrip('\n') for line in open('fizzbuzz.txt')]
dim = len(lines) + 2 #nums + fizz + buzz
print dim
X, Y = prepare_data(lines, dim)
print "data prepared"

#print X, Y
ml_train = True
if ml_train:
    #early_stopping = EarlyStopping(monitor='acc', patience=800)
    fb_model = Sequential()
    fb_model.add(Dense(output_dim=inner_layer, input_dim=dim))
    print "stacking:" + str(stacked_layers) + " layers"
    for _ in range(stacked_layers):
        fb_model.add(Dense(output_dim=inner_layer, input_dim=inner_layer))
    fb_model.add(Dense(output_dim=dim, input_dim=inner_layer))
    fb_model.add(Activation('softmax'))
    fb_model.compile(loss='categorical_crossentropy', optimizer='sgd')
    print "Training data with shape: ", X.shape, " we gonna train for nb_epochs:", nb_epochs
    print fb_model.summary()
    fb_model.fit(X, Y, batch_size=64, nb_epoch=nb_epochs, verbose=1, sample_weight=None, show_accuracy=True)

    predictions = fb_model.predict(X, batch_size=64, verbose=1)
    f = open("results.txt", "w")
    for i, pred in enumerate(predictions):
        fizz = ""
        buzz = ""
        num = ""
        #print pred
        nonzeroind = np.argmax(pred)
        if dim-2 == nonzeroind:
            fizz = "fizz"
            pred[nonzeroind] = 0
            tmp_nonz = nonzeroind
            nonzeroind = np.argmax(pred)
            #print  pred[nonzeroind]
            if pred[nonzeroind] < 0.25:
                nonzeroind = tmp_nonz
        if dim-1 == nonzeroind:
            buzz = "buzz"
        if fizz is "" and buzz is "":
            num = nonzeroind

        to_file = str(i+1) + " " + str(num) + fizz + buzz + "\n"
        f.write(to_file)
