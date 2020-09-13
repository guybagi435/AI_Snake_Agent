import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import random
import numpy as np
tensorflow.compat.v1.logging.set_verbosity(tensorflow.compat.v1.logging.ERROR) 
class agent:
    def __init__(self,index,weights=None):
        self.index=index
        self.scores=0
        self.nn=None
        self.create_NN(weights)
    
    def create_NN(self,weights=None):
        if weights==None:
            initializer=tensorflow.keras.initializers.RandomNormal(mean=1, stddev=0.5,seed=self.index)
            #initializer=tensorflow.keras.initializers.GlorotUniform(self.index)
            model=Sequential()
            model.add(Dense(8, input_shape=(12,),use_bias=False, kernel_initializer=initializer,activation='relu'))
            # model.add(Dense(8,use_bias=False, activation='relu'))
            model.add(Dense(5,use_bias=False, kernel_initializer=initializer,activation='softmax'))
            self.nn=model
        else:
            initializer = tensorflow.keras.initializers.Zeros()
            model=Sequential()
            model.add(Dense(12, input_shape=(10,),kernel_initializer=initializer,use_bias=False, activation='relu'))
             # model.add(Dense(8,use_bias=False, activation='relu'))
            model.add(Dense(5,use_bias=False,kernel_initializer=initializer, activation='softmax'))
            model.set_weights(weights)
            self.nn=model

    def key(self,input_val):
        #print(self.nn.predict(input_val.reshape((-1,10)))[0][0])
        return np.argmax(self.nn.predict(input_val.reshape((-1,12))),axis=-1)[0]
    
    def evolve(self):
        evolve_val=0.02
        weights=self.nn.get_weights()
        for a in range(len(weights)):
            for b in range(len(weights[a])):
                for c in weights[a][b]:
                    c+=evolve_val*np.random.randn()
        return weights
    def update(self,weights):
        self.nn.set_weights(weights)
    


       
