from xml.dom.minidom import Document
from xml.dom.xmlbuilder import DocumentLS
import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from pyparsing import Word
import numpy as np
import tensorflow as tf
import tflearn
import random
import json
with open('intents.json',encoding='utf-8') as file:
    intents=json.load(file)
    
words = []
classes = []
documents = []
stop_words = ['đó','gì','đi','mấy','là']

for intent in intents['intents']:
    for pattern in intent['patterns']:

        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words if w not in stop_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

training = []
output = []
output_empty = [0] * len(classes)
for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [word.lower() for word in pattern_words]
    for m in words:
        bag.append(1) if m in pattern_words else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])
random.shuffle(training)
training = np.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])
print(len(train_x[0]))

import pickle
pickle.dump({'words':words,'classes':classes,'train_x':train_x,'train_y':train_y},open("training_data","wb"))
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,len(train_y[0]), activation='softmax')
net = tflearn.regression(net, optimizer='adam',loss='categorical_crossentropy')

model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
model.fit(train_x,train_y,n_epoch=1000,batch_size=8,show_metric=True)
model.save('train\model.tflearn')
