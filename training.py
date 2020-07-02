from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import json
import pickle
import numpy as np

# read dataset for training bot
with open("dataset/one.json", mode="r") as file:
    data = json.load(file)

labels = []
sentences = []
types = []
words = []
answers = []
for key in data:
    answers.append(data[key]['answer'])
    for sentence in data[key]['question']:
        sentences.append(sentence)

        sentence = sentence.split()
        for word in sentence:
            if word not in words:
                words.append(word)

        types.append(key)

    if key not in labels:
        labels.append(key)

# make structure for training ai

# make structure for output
outputs = []
for type in types:
    emy_out = [0 for _ in range(len(labels))]
    emy_out[labels.index(type)] = 1
    outputs.append(emy_out)

outputs = np.array(outputs)

# make structure for input
training = []
for sentence in sentences:
    bag = []
    sentence = sentence.split()
    for word in words:
        if word in sentence:
           bag.append(1)
        else:
            bag.append(0)

    training.append(bag)

training = np.array(training)

# make model for training
model = Sequential()
model.add(Dense(8, input_dim=len(training[0]), activation="relu"))
model.add(Dense(int(len(training[0]) / 2), activation="relu"))
model.add(Dense(int(len(training[0]) / 2), activation="relu"))
model.add(Dense(len(outputs[0]), activation="sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam", metrics="accuracy")
model.fit(training, outputs, epochs=200, batch_size=10)

# save model ai
model.save("model/one.keras")

# save data for training
with open("dataset/words.pickel", mode="wb") as file:
    pickle.dump([words, answers], file)
