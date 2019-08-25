import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout,LSTM, BatchNormalization
from keras.optimizers import Adam
from scipy.io.wavfile import read
import soundops

BATCH_SIZE=32
HID_1=32 #number of neurons is LSTM layer
DENSE_LAYER=100 #number of neurons of Dense Layer, must match Timesteps
TIMESTEPS=DENSE_LAYER #number of samples fed in 
EPOCHS=10
save_model=True #if you think model is good, then set save_model to true
def create_model(TIMESTEPS):
    model = Sequential()
    model.add(LSTM(32, input_shape=(TIMESTEPS,1), return_sequences=True))
    #model.add(Dropout(0.2))
    model.add(LSTM(32, return_sequences=False))
    model.add(Dense(TIMESTEPS))
    model.compile(loss='mse', optimizer=Adam(0.001), metrics=['acc'])
    return model
#def normalization(data):
#    maxval = np.argmax(data)
#    minval = np.argmin(data)
#    diff = maxval - minval
#    finalarray = []
#    for val in data:
#        finalarray.append((val - minval) / diff)
#    return np.asarray(finalarray)


#def betternormalization(data):
#    minhigh = None
#    maxlow = 0
#    for i in data:
#        minhigh = min(minhigh, i)
#        maxlow = max(maxlow, i)


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
noised=soundops.data_to_chunks(noised, TIMESTEPS) 
noised=np.stack(noised) #concatenate stuffs
noised=noised.astype("float32")

audiodata=soundops.data_to_chunks(audiodata, TIMESTEPS)
audiodata=np.asarray(audiodata,dtype='float32') #float32 for fast GPU






noised = noised.reshape((len(noised),TIMESTEPS,1))
model=create_model(TIMESTEPS)
model.fit(noised, audiodata, epochs=EPOCHS, batch_size=BATCH_SIZE)
if save_model:
    model.save("./models/first_model.h5")