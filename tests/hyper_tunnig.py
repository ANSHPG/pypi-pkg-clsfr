from classifier_anshp import hyper_tunner,model

from tensorflow.keras.datasets import imdb

# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


(train_x,train_y),(test_x,test_y) = imdb.load_data(num_words = 10000)

word_index = imdb.get_word_index()

reverse_word_index = dict(
 [(value, key) for (key, value) in word_index.items()])

decoded_review = " ".join(
 [reverse_word_index.get(i - 3, "?") for i in train_x[0]])

import numpy as np
def vectorize_sequences(sequences, dimension=10000):
     results = np.zeros((len(sequences), dimension)) 
     for i, sequence in enumerate(sequences):
         for j in sequence:
             results[i, j] = 1. 
     return results
x_train = vectorize_sequences(train_x) 
x_test = vectorize_sequences(test_x)

y_train = np.asarray(train_y).astype("float32")
y_test = np.asarray(test_y).astype("float32")

x_val = x_train[:10000]
partial_x_train = x_train[10000:]

y_val = y_train[:10000]
partial_y_train = y_train[10000:]

print(len(partial_x_train))

hyper_tunner(partial_x_train,partial_y_train,x_val,y_val,5,0)

module = model()

pred = module.predict(x_test)
print(pred)