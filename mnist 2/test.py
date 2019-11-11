import tensorflow as tf  # deep learning library. Tensors are just multi-dimensional arrays
import sys,os,cv2,numpy as np


def list_files(target):
    files = []
    for p, _, f in os.walk(os.path.abspath(target)):
        i = 0
        for file_name in f:
            i += 1
            file_name = str(file_name)
            f = file_name.split('_')[1]
            file_class = int(f.split('.jpeg')[0].split('class=')[1])
            files.append((file_name, file_class))
    return files

# Converte as imagens p/ entrada de uma rede neural.
def load_data(target):
    files = list_files(target)
    x,y = [],[]
    for f_name,f_class in files:
        img = cv2.imread(target+f_name,0)
        xi = []
        for l in img:
            for c in l:
                xi.append(c)
        xi = np.array(xi)
        
        x.append(xi)
        y.append(f_class)
    x= np.array(x)
    y= np.array(y)
    return (x,y)



# mnist = tf.keras.datasets.mnist  # mnist is a dataset of 28x28 images of handwritten digits and their labels
(x_train, y_train) = load_data('./train/')
(x_test, y_test) = load_data('./val/')



x_train = tf.keras.utils.normalize(x_train, axis=1)  # scales data between 0 and 1
x_test = tf.keras.utils.normalize(x_test, axis=1)  # scales data between 0 and 1

model = tf.keras.models.Sequential()  # a basic feed-forward model
model.add(tf.keras.layers.Flatten())  # takes our 28x28 and makes it 1x784
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))  # our output layer. 10 units for 10 classes. Softmax for probability distribution

model.compile(optimizer='adam',  # Good default optimizer to start with
              loss='sparse_categorical_crossentropy',  # how will we calculate our "error." Neural network aims to minimize loss.
              metrics=['accuracy'])  # what to track

model.fit(x_train, y_train, epochs=3)  # train the model

val_loss, val_acc = model.evaluate(x_test, y_test)  # evaluate the out of sample data with model
print(val_loss)  # model's loss (error)
print(val_acc)  # model's accuracy
