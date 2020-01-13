#!/usr/bin/env python
# coding: utf-8

# In[70]:


import numpy as np
import math
import matplotlib.pyplot as plt # to plot error during training
mat = np.identity(200)#need change
P={}
epochs=0
songList=[]
hate=[0]*200
like=[0]*200
test=[]
f = open("songList.txt", 'r')
while True:
    line = f.readline()[:-1]
    if not line: break
    songList.append(line)
f.close()


f = open("random_test.txt", 'r')
while True:
    line = f.readline()[:-1]
    if not line: break
    test.append(line)
f.close()


# In[71]:


def isLike(a, b):
    if(test.index(b)-test.index(a)!=1):
        if(test.index(a)!=0 or test.index(b)!=199):
            return False
    return True


# In[72]:


Euclidean = np.loadtxt('Euclidean.txt', usecols=range(200))


# In[73]:


def normalize(a):
    for i in range(a.shape[0]):
        tot=0
        for j in range(a.shape[1]):
            if(a[i, j]!=0):
                a[i, j]=1/a[i, j]
            tot+=a[i,j]
        for j in range(a.shape[1]):
            a[i, j]=a[i, j]/tot
    return a
Euclidean=(normalize(Euclidean))
#for i in range(Euclidean.shape[0]):
#    tot=0
#    for j in range(Euclidean.shape[1]):
#        tot+=Euclidean[i,j]
#    print(tot)


# In[74]:


mat=Euclidean
like_mat=np.zeros((len(test), len(test)))


# In[109]:


for i in test:
    for j in test:
        if(isLike(i, j)):
            like_mat[songList.index(i),songList.index(j)]=1


# In[ ]:





# In[110]:


# input data
inputs = np.identity(200)
# output data
outputs = like_mat #interest of the uses, need change


# In[111]:


class NeuralNetwork():
    global epochs
    global hate
    global like
    # intialize variables in class
    def __init__(self, inputs, outputs):
        self.inputs  = inputs
        self.outputs = outputs
        # initialize weights as .50 for simplicity
        self.weights = mat
        self.error_history = []
        self.epoch_list = []

    def sigmoid(self, x, deriv=False):
        if deriv == True:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

    # data will flow through the neural network.
    def feed_forward(self):
        self.hidden = self.sigmoid(np.dot(self.inputs, self.weights))

    # going backwards through the network to update weights
    def backpropagation(self):
        self.error  = self.outputs - self.hidden
        delta = self.error * self.sigmoid(self.hidden, deriv=True)
        self.weights += np.dot(self.inputs.T, delta)

    # train the neural net for 25,000 iterations
    def train(self, reqEpoch=3000):
        for epochs in range(reqEpoch):
            # flow forward and produce an output
            self.feed_forward()
            # go back though the network to make corrections based on the output
            self.backpropagation()    
            # keep track of the error history over each epoch
            self.error_history.append(np.average(np.abs(self.error)))
            self.epoch_list.append(epochs)
            epochs+=1

    # function to predict output on new and unseen input data                               
    def predict(self, new_input):
        prediction = self.sigmoid(np.dot(new_input, self.weights))
        return prediction


# In[112]:



NN = NeuralNetwork(inputs, outputs)
# train neural network
NN.train()

# create two new examples to predict                                   
example = inputs

# print the predictions for both examples                                   
print(NN.predict(example), ' - Correct: ', example)

# plot the error over the entire training duration
plt.figure(figsize=(15,5))
plt.plot(NN.epoch_list, NN.error_history)
plt.xlabel('Epoch')
plt.ylabel('Error')
plt.show()


# In[108]:


for i in range(200):
    for j in range(200):
        if(outputs[i, j]!=0):
            print(outputs[i, j], (i, j))


# In[ ]:





# In[ ]:




