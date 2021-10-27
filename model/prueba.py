from model import make_model

import tensorflow as tf
import tensorflow.keras
import numpy as np

from tensorflow import keras
from tensorflow.keras import layers
import os

image_size = (180, 180)
batch_size = 32

model = make_model(input_shape=image_size + (3,), num_classes=2)
model.load_weights("h5/data_cd.h5")

model0 = make_model(input_shape=image_size + (3,), num_classes=2)
model0.load_weights("h5/data_cd.h5")

model1 = make_model(input_shape=image_size + (3,), num_classes=2)
model1.load_weights("h5/data_cd.h5")

print("modelo1")
for i in os.listdir("dataset/gato/"):
    img = keras.preprocessing.image.load_img(
    f"dataset/gato/{i}", target_size=image_size
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    predictions = model.predict(img_array)
    score = predictions[0]
    print(
        f"This image {i} is %.2f percent cat and %.2f percent dog."
        % (100 * (1 - score), 100 * score)
    )

print("modelo2")
for i in os.listdir("dataset/gato/"):
    img = keras.preprocessing.image.load_img(
    f"dataset/gato/{i}", target_size=image_size
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    predictions = model.predict(img_array)
    score = predictions[0]
    print(
        f"This image {i} is %.2f percent cat and %.2f percent dog."
        % (100 * (1 - score), 100 * score)
    )

print("modelo3")
for i in os.listdir("dataset/gato/"):
    img = keras.preprocessing.image.load_img(
    f"dataset/gato/{i}", target_size=image_size
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    predictions = model.predict(img_array)
    score = predictions[0]
    print(
        f"This image {i} is %.2f percent cat and %.2f percent dog."
        % (100 * (1 - score), 100 * score)
    )

print("termino")
