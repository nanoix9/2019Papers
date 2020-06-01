'''
#This example demonstrates the use of Convolution1D for text classification.

Gets to 0.89 test accuracy after 2 epochs. </br>
90s/epoch on Intel i5 2.4Ghz CPU. </br>
10s/epoch on Tesla K40 GPU.
'''
from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
from keras.datasets import imdb

# set parameters:
max_features = 500
maxlen = 400
batch_size = 32
embedding_dims = 5
filters = 25
kernel_size = 3
hidden_dims = 250
epochs = 2

'''
# More real parameters:
max_features = 5000
maxlen = 400
batch_size = 32
embedding_dims = 50
filters = 250
kernel_size = 3
hidden_dims = 250
epochs = 2
'''

# Parameter tuning

# Epoch 1/2
# 25000/25000 [==============================] - 21s 833us/step - loss: 0.6130 - accuracy: 0.7035 - val_loss: 0.4708 - val_accuracy: 0.8056
# Epoch 2/2
# 25000/25000 [==============================] - 20s 812us/step - loss: 0.4762 - accuracy: 0.8094 - val_loss: 0.4230 - val_accuracy: 0.8296
# max_features = 5000
# maxlen = 400
# batch_size = 32
# embedding_dims = 50
# filters = 25
# kernel_size = 3
# hidden_dims = 250
# epochs = 2

# Epoch 1/2
# 25000/25000 [==============================] - 74s 3ms/step - loss: 0.5686 - accuracy: 0.7342 - val_loss: 0.5026 - val_accuracy: 0.8118
# Epoch 2/2
# 25000/25000 [==============================] - 72s 3ms/step - loss: 0.4819 - accuracy: 0.8161 - val_loss: 0.4400 - val_accuracy: 0.8413
# max_features = 5000
# maxlen = 400
# batch_size = 32
# embedding_dims = 50
# filters = 250
# kernel_size = 3
# hidden_dims = 250
# epochs = 2

# Best accuracy archived: 85.89%
# Epoch 1/2
# 25000/25000 [==============================] - 67s 3ms/step - loss: 0.5496 - accuracy: 0.7384 - val_loss: 0.4080 - val_accuracy: 0.8372
# Epoch 2/2
# 25000/25000 [==============================] - 68s 3ms/step - loss: 0.6776 - accuracy: 0.7964 - val_loss: 0.3827 - val_accuracy: 0.8589
max_features = 5000
maxlen = 400
batch_size = 32
embedding_dims = 80
filters = 150
kernel_size = 3
hidden_dims = 150
epochs = 2



print('Loading data...')
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

print('Build model...')
model = Sequential()

# we start off with an efficient embedding layer which maps
# our vocab indices into embedding_dims dimensions
model.add(Embedding(max_features,
                    embedding_dims,
                    input_length=maxlen))
model.add(Dropout(0.2))

# we add a Convolution1D, which will learn filters
# word group filters of size filter_length:
model.add(Conv1D(filters,
                 kernel_size,
                 padding='valid',
                 activation='relu',
                 strides=1))
# we use max pooling:
model.add(GlobalMaxPooling1D())

# We add a vanilla hidden layer:
model.add(Dense(hidden_dims))
model.add(Dropout(0.2))
model.add(Activation('relu'))

# We project onto a single unit output layer, and squash it with a sigmoid:
model.add(Dense(1))
#model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(x_test, y_test))