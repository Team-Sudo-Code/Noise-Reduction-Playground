import numpy as np
import tensorflow as tf
from keras import models, layers
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv1D, LSTM, BatchNormalization
from keras.optimizers import Adam
from scipy.io.wavfile import read
import soundops
def normalization(data):
    maxval=np.argmax(data)
    minval=np.argmin(data)
    diff=maxval-minval
    finalarray=[]
    for val in data:
        finalarray.append((val-minval)/diff)
    return np.asarray(finalarray)
def preprocessing():
    samplingrate,data=read("Megalovania.wav")
    print("Read data")
    data=normalization(data)
    print("Data normalized")
    return data
def build_model():
    ###Placeholder model
    model=Sequential()
    model.add(LSTM(512,activation='relu', input_dim=2))
    
    model.add(Dense(1,activation='sigmoid'))
    model.compile(loss='categorical_crossentropy', optimizer=Adam(0.001), metrics=['categorical_accuracy'])
    return model
audiodata=preprocessing()
model=build_model()
model.fit(soundops.create_noise(audiodata),audiodata, epochs=1) 