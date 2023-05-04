import numpy as np
import matplotlib as plt
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix


# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train i test podaci
(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()

# prikaz karakteristika train i test podataka
print('Train: X=%s, y=%s' % (train_images.shape, train_labels.shape))
print('Test: X=%s, y=%s' % (test_images.shape, test_labels.shape))

# TODO: prikazi nekoliko slika iz train skupa
plt.figure()
plt.imshow(train_images[0])
plt.title(train_labels[0])
plt.show()

# skaliranje slike na raspon [0,1]
train_images_s = train_images.astype("float32") / 255
test_images_s = test_images.astype("float32") / 255

# slike trebaju biti (28, 28, 1)
train_images_s = np.expand_dims(train_images_s, -1)
test_images_s = np.expand_dims(test_images_s, -1)

print("train_images shape:", train_images_s.shape)
print(train_images_s.shape[0], "train samples")
print(test_images_s.shape[0], "test samples")


# pretvori labele
train_labels_s = keras.utils.to_categorical(train_labels, num_classes)
test_labels_s = keras.utils.to_categorical(test_labels, num_classes)

#reshapeanje matrice sa slikama
train_images_reshaped = train_images_s.reshape(60000,784)
test_images_reshaped = test_images_s.reshape(10000,784)

# TODO: kreiraj model pomocu keras.Sequential(); prikazi njegovu strukturu

model = keras.Sequential()
model.add(layers.Input(shape = (784,)))
model.add(layers.Dense(50, activation = "relu"))
model.add(layers.Dense(10,activation = "softmax"))
model.summary()

# TODO: definiraj karakteristike procesa ucenja pomocu .compile()

model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy",])

# TODO: provedi ucenje mreze


batch_size = 32
epochs = 20
history = model.fit(train_images_reshaped, train_labels,
                    batch_size = batch_size,
                    epochs = epochs,
                    validation_split = 0.1)

# TODO: Prikazi test accuracy i matricu zabune



# TODO: spremi model

