import numpy as np
import tensorflow as tf
from keras import models, layers
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv1D, LSTM, BatchNormalization, Reshape, Embedding
from keras.optimizers import Adam
from scipy.io.wavfile import read
import soundops


def normalization(data):
    maxval = np.argmax(data)
    minval = np.argmin(data)
    diff = maxval - minval
    finalarray = []
    for val in data:
        finalarray.append((val - minval) / diff)
    return np.asarray(finalarray)


def betternormalization(data):
    minhigh = None
    maxlow = 0
    for i in data:
        minhigh = min(minhigh, i)
        maxlow = max(maxlow, i)


def preprocessing():
    samplingrate, data = read("Megalovania.wav")
    print("Read data")
    data = normalization(data)
    print("Data normalized")
    return data

audiodata = preprocessing()
audiodata = [x[0] for x in audiodata]
audiodata=np.asarray(audiodata)


model = Sequential()
model.add(Embedding(len(audiodata),64))
model.add(LSTM(32, return_sequences=False))
model.add(Dense(1))
model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(0.001), metrics=['categorical_accuracy'])
noised = soundops.create_noise(audiodata)
#noised = noised.reshape((1, len(noised), 1))
#audiodata=audiodata.reshape(1,len(audiodata),1)
model.fit(noised, audiodata, epochs=1)
model.save("./models/first_model.h5")