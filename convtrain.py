# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:09:29 2019

@author: Li Wende
"""

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout,Conv2D, BatchNormalization, UpSampling2D, MaxPooling2D
from keras.optimizers import Adam
from scipy.io.wavfile import read
from sklearn.preprocessing import MinMaxScaler
import soundops
import cv2

BATCH_SIZE=32
HID_1=32 #number of neurons in CONV1D layer
TIMESTEPS=100 
EPOCHS=10
save_model=True #if you think model is good, then set save_model to true

def preprocessing():
    min_max=MinMaxScaler()
    samplingrate, audiodata = read("Megalovania.wav")
    print("Read data")
    audiodata=min_max.fit_transform(audiodata.reshape(-1,1))
    print("Scaled data")
    audiodata=audiodata.reshape(len(audiodata))
    return (audiodata,samplingrate)
def create_model():
    #autoencoder style model
    model=Sequential()
    model.add(Conv2D(100,(5,5), input_shape=(480,640,3), activation='relu', padding='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.4))
    model.add(Conv2D(75,(3,3), activation='relu', padding='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.4))
    model.add(Conv2D(50,(3,3), activation='relu', padding='same'))
    model.add(UpSampling2D(size=(2, 2)))
    model.add(Dropout(0.4))
    model.add(Conv2D(75,(3,3), activation='relu', padding='same'))
    model.add(UpSampling2D(size=(2,2)))
    model.add(Dropout(0.4))
    model.add(Dense(20, activation='sigmoid'))
    model.compile(loss='mse', optimizer=Adam(0.01), metrics=['acc'])
    return model
audiodata,samplingrate=preprocessing()
#audiodata = [x[0] for x in audiodata]
audiodata=np.asarray(audiodata,dtype='float32')
soundops.gen_specgram(audiodata,512,samplingrate)
data=cv2.imread("image.png")
noised=soundops.create_noise(audiodata)
data=soundops.data_to_chunks(data, 20)
model=create_model()
model.fit(data,audiodata,validation_split=0.2, epochs=EPOCHS,batch_size=20)


