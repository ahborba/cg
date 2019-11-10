import sklearn.metrics as metrics
import tensorflow as tf
import numpy as np 
from numpy.random import seed
seed(1)
class NN:

    def __init__(self,x,y,epoch):
        self.epoch = epoch
        self.x = x
        self.y = y
        self.model = tf.keras.models.Sequential()
        

    def add_layer(self,neurons,act = tf.nn.sigmoid):
        self.model.add(tf.keras.layers.Dense(neurons, activation=act))
    
    def normalize(self,x,axis=1):
        self.x =  tf.keras.utils.normalize(x,axis)
    
    def train(self):
        self.model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
        return self.model.fit(self.x, self.y, epochs=self.epoch)  # train the model

    def confusion_matrix(self,real_values,predictions):
        cm = metrics.confusion_matrix(real_values, predictions,labels=[0,1,2,3,4,5,6,7,8,9])
        return np.around(cm/cm.astype(np.float).sum(axis=1),2)
    
        
    def predict(self,x):
        return self.model.predict(x)
    
    def evaluate(self,x,y):
         return self.model.evaluate(x,y)