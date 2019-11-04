import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.utils import to_categorical
import time,json

np.random.seed(0)

class NN(object):
    """
    A network that uses Sigmoid activation function.
    """

    def __init__(self):

        self.nodes = []
        self.layers = {}
        self.weights = {}
        self.n_classes = 10
        self.higher = 0    
        self.w = {}
        self.l = {}

        # For Debugging
        self.grads = {}
        self.regs = {}
        self.dels = {}
        self.train_history=[]

        # For analysis
        self.history = {}

    def add_layer(self, n_nodes, output_layer=False):
        """
        Adds a layer of specified no. of output nodes.
        For the output layer, the flag  output_layer must be True.
        A network must have an output layer.
        """

        if not output_layer:
            self.nodes.append(n_nodes)
        else:
            self.n_classes = n_nodes

    def sigmoid(self, z):
        """
        Calculates the sigmoid activation function.
        """

        return 1 / (1 + np.exp(-z))

    def predict(self, x, to_predict=True, argmax=True, rand_weights=False):
        """
        Performs a pass of forward propagation.
        If to_predict is set to True, trained weights are used
        and predictions are returned in a single vector
        with labels from 0 to (n_classes - 1).
        """
    
        nodes = self.nodes
        layers = {}
        weights = {}
    
        # -------------- for input layer
        m = x.shape[0]
        x = np.append(np.ones(m).reshape(m, 1), x, axis=1)
        layers['a%d' % 1] = x
    
        # --------------- for dense layers
        for i in range(len(nodes)):
            m, n = x.shape
            w = np.random.randn(nodes[i], n) if rand_weights else self.weights['w%d' % (i + 1)]
            z = x.dot(w.T)
            a = np.append(np.ones(m).reshape(m, 1), self.sigmoid(z), axis=1)
    
            if not to_predict:
                layers['a%d' % (i + 2)] = a # We start from a2, as a1 is already done.
                weights['w%d' % (i + 1)] = w # We start from w1
            x = a # to repeat the same procedure for the next layer.
    
        # --------------- for output layer
        m, n = x.shape
        w = np.random.randn(self.n_classes, n) if rand_weights else self.weights['w%d' % (len(nodes) + 1)]
        z = x.dot(w.T)
        a = self.sigmoid(z)
        output = a
    
        if not to_predict:
            layers['a%d' % (len(layers) + 1)] = a
            weights['w%d' % (len(weights) + 1)] = w
    
        if to_predict:
            return np.argmax(output, axis=1)
        elif rand_weights:
            self.layers = layers
            self.weights = weights
        else:
            return layers, weights

    def cost(self, x, y, lamda=0):
        """
        Calculates the cost for given data and labels, with trained weights.
        """

        weights = self.weights
        layers, _ = self.predict(x, to_predict=False)

        m, n = x.shape
        reg2 = 0
        for i in range(len(weights)):
            reg2 += np.sum(weights['w%d' % (i + 1)][:, 1:] ** 2)

        j = (-1 / m) * np.sum(y.T.dot(np.log(layers['a%d' % (len(layers))])) +
                              (1 - y).T.dot(np.log(1 - layers['a%d' % (len(layers))]))) + (lamda / (((2 * m)) * reg2)+0.000000001)

        return j

    def fit(self, data, labels, test=[], test_labels=[], alpha=0.01, lamda=0, epochs=50):
         # ----------- Checking data format
        assert self.n_classes, 'You must have the output layer. Set output_layer=True while adding the output layer.'
        assert (labels.shape[0] == data.shape[0]), 'The labels must have same no. of rows as training data.'
        assert (labels.shape[1] == self.n_classes), 'The labels should have same no. of columns as there are ' \
                                                    'classes. Convert labels into categorical form before training.'
        assert (epochs > 0), 'No. of epochs must be greater than or equal to 1.'
        assert (len(test) == len(test_labels)), "Invalid combination of test set and test_labels provided." \
                                                "Please check the provided test and test_labels."
        accs=[]
        taccs=[]
        # ------------- Training
        start = time.time()
        self.predict(data, to_predict=False, rand_weights=True)
        j_history = []
        j_test_history = []
        
        for epoch in range(epochs):
            layers, weights = self.predict(data, to_predict=False, rand_weights=False)
            m, n = data.shape
            # ----------------- Calculating del terms
            delta1 = layers['a%d' % (len(layers))] - labels
            delta = delta1.dot(weights['w%d' % (len(weights))]) * layers['a%d' % (len(layers) - 1)] * \
                    (1 - layers['a%d' % (len(layers) - 1)])

            dels = {
                'del%d' % (len(layers)): delta1,
                'del%d' % (len(layers) - 1): delta
            }

            for i in range(len(weights) - 2):
                delta = delta[:, 1:].dot(weights['w%d' % (len(layers) - 2 - i)]) * \
                        layers['a%d' % (len(layers) - 2 - i)] * (1 - layers['a%d' % (len(layers) - 2 - i)])
                dels['del%d' % (len(layers) - 2 - i)] = delta

            # ------------------ Calculating grad and regularization terms
            grads = {
                'grad%d' % (len(weights)): (1 / m) * (
                    dels['del%d' % (len(layers))].T.dot(layers['a%d' % (len(weights))]))
            }

            regs = {
                'reg%d' % (len(weights)): (lamda / m) * weights['w%d' % (len(weights))]
            }

            for i in range(len(weights) - 1):
                grad = (1 / m) * \
                       (dels['del%d' % (len(layers) - 1 - i)][:, 1:].T.dot(layers['a%d' % (len(weights) - 1 - i)]))

                grads['grad%d' % (len(weights) - 1 - i)] = grad

                reg = (lamda / m) * weights['w%d' % (len(weights) - 1 - i)]
                reg[:, 0] = 0
                regs['reg%d' % (len(weights) - 1 - i)] = reg

            # -------------- for debugging later on
            self.grads = grads
            self.regs = regs
            self.dels = dels

            # ----------------- Updating Parameters
            for i in range(1, len(weights) + 1):
                weights['w%d' % i] = weights['w%d' % i] - alpha * grads['grad%d' % i] - regs['reg%d' % i]

            self.layers = layers
            self.weights = weights

            # ----------------- Analysis steps

            j = float(self.cost(data, labels, lamda=lamda))
            j_history.append(j)


            acc = 100 * np.sum(np.argmax(layers['a%d' % (len(layers))], axis=1) == np.argmax(labels, axis=1)) / m
            if acc > self.higher:
                self.higher = acc
                self.w = self.weights
                self.l = self.layers
            accs.append(acc)
            if len(test):
                m1, n1 = test.shape
                j_test = float(self.cost(test, test_labels, lamda=lamda))
                j_test_history.append(j_test)
                test_prediction = self.predict(test)
                acc_test = 100 * np.sum(test_prediction == np.argmax(test_labels, axis=1)) / m1
                # print(epoch)
                taccs.append(acc_test)
                print('Train cost: %0.2f\tTrain acc.: %0.2f%%\tTest cost: %0.2f\tTest acc.: %0.2f%%' % (j, acc, j_test, acc_test))

            else:
                print(epoch,' - cost: %0.2f\tacc.: %0.2f%%' % (j, acc))

        print("Displaying Cost vs Iterations graph...")

        if len(test):
            plot_test, =plt.plot(range(epochs), accs, 'r')

        plot_train, =plt.plot(range(epochs), accs, 'b')
        plt.xlabel('Iterations')
        plt.ylabel('Acc')

        if len(test):
            plot_test, =plt.plot(range(epochs), accs, 'r')
            plt.legend([plot_test, plot_train], ['Test', "Train"])
        else:
            plt.legend([plot_train], ["Train"])

        plt.show()

        cm = pd.crosstab(np.argmax(self.layers['a%d' % (len(self.layers))], axis=1), np.argmax(labels, axis=1),
                         rownames=['Actual'], colnames=['Predicted'])

        end = time.time()

        if len(test):
            print('Final train cost: %0.2f\tFinal train acc.: %0.2f%%\tFinal test cost: %0.2f\tFinal test acc.: %0.2f%%' % (j, acc, j_test, acc_test))
        else:
            print('Final cost: %0.2f\tFinal acc.: %0.2f%%' % (j, acc))
        print('Execution time: %0.2fs' % (end - start))

        self.history['run%d' % (len(self.train_history) + 1)] = {
            'layers': self.nodes,
            'alpha': alpha,
            'lambda': lamda,
            'epochs': epochs,
            'Final train acc.': acc,
            'Final train cost': j,
            'Final test acc.': acc_test if len(test) else 'N/A',
            'Final test cost': j_test if len(test) else 'N/A',
            'Execution time': (end - start)
        }

# --------------- Sample run

def load_data(target,to_predict = False):
    x_list,y_list,es = [],[],[]
    with open(target) as f:
        for line in f:
            line = line.split(',')
            # print(line[-1])
            # input()
            y =int(line[-1])
            if to_predict:
                es.append(y)
            y = to_categorical(y,10)
            y_list.append(y)
            line.pop()
            x_list.append([float(v) for v in line])
    if to_predict:
        return(x_list,y_list,es)
    return(x_list,y_list)

def print_data(d):
    for a in d:
        print(a,end=',')
        for c in d[a]:
            print(*c,sep=',',end='')
        print()

def read_model():
    w,l = {},{}
    with open('./csv/model.csv') as md:
        for line in md:
            line = line.split(',')
            if line[0].startswith('a'):
                layer = line[0]
                line.pop(0)
                l[layer] = [float(lay) for lay in line]
            elif line[0].startswith('w'):
                weight = line[0]
                line.pop(0)
                w[weight] = [float(wei) for wei in line]
    return (w,l)

def train():
    x,y = load_data('./csv/train.csv')
    x = np.array(x)
    y = np.array(y)
    model = NN()
    model.add_layer(10, output_layer=True)
    model.fit(x, y,epochs=200000)
    # write_dict('weights.txt',model.weights)
    # write_dict('layers.txt',model.layers)
    print('higher: ',model.higher,'\n\n\n\n')
    model.layers = model.l
    model.weights = model.w
    print_data(model.l)
    print_data(model.w)
def predict():
    model = NN()
    model.weights,model.layers = read_model()
    x,y,esperado = load_data('./csv/val.csv',True)
    x = np.array(x)
    y_resultado = model.predict(x)
    cont=0
    for i in range(0,len(y_resultado)):
        if esperado[i] == y_resultado[i]:
            cont+=1
    print(cont)
if __name__ == "__main__":
    # train()
    predict()
   
    


