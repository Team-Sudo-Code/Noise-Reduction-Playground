import numpy as np
import tensorflow as tf
from keras import models, layers
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv1D, LSTM
from keras.optimizers import Adam
import soundops
def preprocessing():
    data=soundops.process_all("Megalovania.wav")
    return data
def build_model():
    ###Placeholder model
    model=Sequential()
    model.add(LSTM(512,activation='relu', input_shape=)
    model.add(Dense(20),activation='sigmoid')
    model.compile(loss='categorical_crossentropy', optimizer=Adam(0.001), metrics=['categorical_accuracy'])
audiodata=preprocessing()
#model=build_model()
#model.fit() 