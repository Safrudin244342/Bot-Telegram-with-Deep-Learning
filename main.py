import telepot
from telepot.loop import MessageLoop
import time
from tensorflow.keras.models import load_model
import pickle
import random
import numpy as np

token = # insert your token
TelegramBot = telepot.Bot(token=token)

# load ai model
model = load_model("model/one.keras")

# load words
with open("dataset/words.pickel", mode="rb") as file:
    words, answer = pickle.load(file)

# convert sentence to structure input ai
def bag_sentence(sentence):
    global words
    sentence = sentence.lower()
    sentence = sentence.split()

    bag = []
    for word in words:
        if word in sentence:
            bag.append(1)
        else:
            bag.append(0)

    return np.array([bag])[:]

# reply message from client
def handleChat(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        sentence = bag_sentence(msg['text'].lower())
        result = np.argmax(model.predict(sentence))
        reply = random.choice(answer[result])
        TelegramBot.sendMessage(chat_id, reply)


MessageLoop(TelegramBot, handleChat).run_as_thread()
print("Listening...............")
while True:
    time.sleep(10)
