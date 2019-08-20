import numpy as np
import tensorflow as tf
from keras import models, layers
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv1D, LSTM, BatchNormalization, Reshape, Embedding
from keras.optimizers import Adam
from scipy.io.wavfile import read
import soundops


#def normalization(data):
#    maxval = np.argmax(data)
#    minval = np.argmin(data)
#    diff = maxval - minval
#    finalarray = []
#    for val in data:
#        finalarray.append((val - minval) / diff)
#    return np.asarray(finalarray)


def betternormalization(data):
    minhigh = None
    maxlow = 0
    for i in data:
        minhigh = min(minhigh, i)
        maxlow = max(maxlow, i)


def preprocessing():
    samplingrate, data = read("Megalovania.wav")
    print("Read data")
    #data = normalization(data)
    #print("Data normalized")
    return data

audiodata = preprocessing() #read data
audiodata = [x[0] for x in audiodata] #take L channel of audio
audiodata=np.asarray(audiodata,dtype='float32') #float32 for fast GPU
noised = soundops.create_noise(audiodata)
noised=soundops.data_to_chunks(noised) #200 timesteps per thingamabob

noised=np.stack(noised) #concatenate stuffs
noised=noised.astype("float32")

def create_model():
    model = Sequential()
    model.add(LSTM(32, input_shape=(200,1), return_sequences=False))
    model.add(Dense(200))
    model.compile(loss='mse', optimizer=Adam(0.001), metrics=['acc'])
    return model

noised = noised.reshape((len(noised),200,1))
#audiodata=audiodata.reshape((len(audiodata),200,1))
model=create_model()
model.fit(noised, audiodata, epochs=1)
#model.save("./models/first_model.h5")