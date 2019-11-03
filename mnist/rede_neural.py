from keras.datasets import mnist,to_categorical
from matplotlib import pyplot
import sys
try:
    target = sys.argv[1]
    target = './csv/'+target if not target.startswith('./csv/') else target
except:
    print("Insira o nome do objeto desejado e tente novamente.")
    exit()

# load dataset
(trainX, trainy), (testX, testy) = mnist.load_data()
print(len(trainy),len(trainX))
exit()
# summarize loaded dataset
print('Train: X=%s, y=%s' % (trainX.shape, trainy.shape))
print('Test: X=%s, y=%s' % (testX.shape, testy.shape))
# plot first few images
for i in range(9):
	# define subplot
	pyplot.subplot(330 + 1 + i)
	# plot raw pixel data
	pyplot.imshow(trainX[i], cmap=pyplot.get_cmap('gray'))
# show the figure
pyplot.show()


# load train and test dataset
def load_dataset():

	# load dataset
	(trainX, trainY), (testX, testY) = mnist.load_data()
	# reshape dataset to have a single channel
	trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
	testX = testX.reshape((testX.shape[0], 28, 28, 1))
	# one hot encode target values
	trainY = to_categorical(trainY)
	testY = to_categorical(testY)
	return trainX, trainY, testX, testY