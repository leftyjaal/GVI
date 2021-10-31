# from model import make_model
from cnn.model import make_model
import tensorflow as tf
import tensorflow.keras
import numpy as np

from tensorflow import keras
from tensorflow.keras import layers
import os


def model_prediction(path, weight_path):
    the_list = []
    labels = ()
    image_size = (180, 180)
    batch_size = 32

    if weight_path == "hierarchical/data_cd.h5":
        labels = ("Cat", "Dog")
    if weight_path == "hierarchical/data_fpl.h5":
        labels = ("Food", "Plant")
    if weight_path == "hierarchical/data_lpe.h5":
        labels = ("Landscape", "People")

    # print(labels)

    model = make_model(input_shape=image_size + (3,), num_classes=2)
    model.load_weights(weight_path)

    for i in os.listdir(path):
        img = keras.preprocessing.image.load_img(
            f"{path}{i}", target_size=image_size
        )
        # print("#########################")
        # print(f"{path}{i}")
        # print("#########################")
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create batch axis
        predictions = model.predict(img_array)
        score = predictions[0]
        # print(
        #     f"This image {i} is %.2f percent {labels[0]} and %.2f percent {labels[1]}."
        #     % (100 * (1 - score), 100 * score)
        # )

        label = ""
        value = 0
        label1 = 100 * (1 - score)
        label2 = 100 * score

        if label1 > label2:
            label = labels[0]
            value = label1
        else:
            label = labels[1]
            value = label2

        the_list.append(Image(f"{path}{i}", label, value))

    tf.keras.backend.clear_session()
    return the_list
    # sort_list(first_list)


def sort_list(thelist):
    # print("sort")
    # for obj in thelist:
    #     print(obj.label, obj.path, obj.value)

    thelist.sort(key = lambda x : x.label)
    # print("----------------")
    # for ojb in thelist:
    #     print(ojb.label, ojb.path, ojb.value)

    # print("end sort")
    return thelist


def merge_list(list1, list2, list3):
    list_merged = []
    list_cache = []
    for i in range(len(list1)):
        if list1[i].value > list2[i].value:
            list_cache.append(list1[i])
        else:
            list_cache.append(list2[i])

    for j in range(len(list_cache)):
        if list3[j].value > list_cache[j].value:
            list_merged.append(list3[j])
        else:
            list_merged.append(list_cache[j])

    return list_merged


def classifier_main(request_folder):
    cd_list = model_prediction(request_folder, "hierarchical/data_cd.h5")

    fpl_list = model_prediction(request_folder, "hierarchical/data_fpl.h5")

    lpe_list = model_prediction(request_folder, "hierarchical/data_lpe.h5")

    lista = merge_list(cd_list, fpl_list, lpe_list)
    class_list = sort_list(lista)
    # print(class_list[0].path)
    print("Classification finished")
    return class_list


# Image object
class Image:
    def __init__(self, path, label, value):
        self.path = path
        self.label = label
        self.value = value
