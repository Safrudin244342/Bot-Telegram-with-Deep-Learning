# Bot-Telegram-with-Deep-Learning

Aplikasi Bot Telegram sederhana dengan mengimplementasikan deep learning

**Daftar File**

*1. dataset/one.json*
```bash
"hay": {
    "question": ["hay", "hallo", "selamat pagi", "good morning", "selamat sore", "good evening", "selamat malam", "good night"],
    "answer": ["hay", "hallo", "hey, how i can help you?"]
  }
```

File ini berisi daftar pertanyaan dan jawaban, file ini yang akan digunakan untuk training deep learning, kamu bisa mengganti atau menambah pertanyaan dan jawabanya melalui file ini

*2. training.py*

File ini digunakan untuk mentraining deep learning berdasarkan list pertanyaan dan jawaban dari file dataset/one.json

membaca file dataset/one.json
```bash
line 8 file training.py

with open("dataset/one.json", mode="r") as file:
    data = json.load(file)
```

membuat layer untuk training deep learning
```bash
line 58 file training.py

model = Sequential()
model.add(Dense(8, input_dim=len(training[0]), activation="relu"))
model.add(Dense(int(len(training[0]) / 2), activation="relu"))
model.add(Dense(int(len(training[0]) / 2), activation="relu"))
model.add(Dense(len(outputs[0]), activation="sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam", metrics="accuracy")
model.fit(training, outputs, epochs=200, batch_size=10)
```

proses training data
```bash
Epoch 46/50
4/4 [==============================] - 0s 1ms/step - loss: 0.2881 - accuracy: 0.5789
Epoch 47/50
4/4 [==============================] - 0s 2ms/step - loss: 0.2833 - accuracy: 0.5789
Epoch 48/50
4/4 [==============================] - 0s 1ms/step - loss: 0.2784 - accuracy: 0.5789
Epoch 49/50
4/4 [==============================] - 0s 1ms/step - loss: 0.2737 - accuracy: 0.5789
Epoch 50/50
4/4 [==============================] - 0s 1ms/step - loss: 0.2687 - accuracy: 0.6053
```

menyimpan model training
```bash
line 67 file training.py

model.save("model/one.keras")
```

menyimpan daftar words
```bash
line 70 file training.py

with open("dataset/words.pickel", mode="wb") as file:
    pickle.dump([words, answers], file)
```

*3. main.py*

File ini yang menghandle pesan masuk dan menentukan balasannya

Menentukan token dari bot telegram
```bash
line 7 file main.py

token = "************************************"
```

Load model deep learning
```bash
line 13 file main.py

model = load_model("model/one.keras")
```

Load list words and answer
```bash
line 16 file main.py

with open("dataset/words.pickel", mode="rb") as file:
    words, answer = pickle.load(file)
```

Memprediksi jawaban yang paling sesuai dari pertanyaan yang diajukan
```bash
line 47 file main.py

result = np.argmax(model.predict(sentence))
reply = random.choice(answer[result])
```
