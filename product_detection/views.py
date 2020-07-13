from django.shortcuts import render
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings 
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.imagenet_utils import decode_predictions
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras import Sequential
import datetime
import traceback
import os
import shutil
import pandas as pd


def index(request):
    prior = ResNet50(include_top=False,
                     weights='imagenet',
                    input_shape=(224, 224, 3))
    model = Sequential()
    model.add(prior)
    model.add(tf.keras.layers.GlobalAveragePooling2D(name='GA'))
    model.add(Flatten(name='Flatten'))
    model.add(Dense(1024, activation='linear', name='Dense1'))
    model.add(Dense(512, activation='linear', name='Dense2'))
    model.add(Dense(256, activation='linear', name='Dense3'))
    model.add(Dense(128, activation='linear', name='Dense4'))
    model.add(Dense(64, activation='linear', name='Dense5'))
    model.add(Dense(42, activation='softmax', name='Output'))
    opt = tf.keras.optimizers.RMSprop()
    model.compile(
        optimizer=opt,
        loss='categorical_crossentropy',
        metrics=[tf.keras.metrics.TopKCategoricalAccuracy(1)]
    )
    model.load_weights(os.path.join(settings.BASE_DIR,'weights', 'weights.hdf5'))


    if  request.method == "POST":
        try:
            shutil.rmtree(os.path.join(settings.BASE_DIR, 'media'))
        except:
            pass
        f = request.FILES['sentFile'] # here you get the files needed
        response = {}
        file_name = "pic.jpg"
        name = default_storage.save(file_name, f)
        response['file_url'] = default_storage.url(name)
        
        
        datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1./255
        )
        generator = datagen.flow_from_directory(
            os.path.join(settings.BASE_DIR, 'media'),
            target_size=(224, 224),
            batch_size=128,
            shuffle=False,
            class_mode=None
        )
        generator.reset()

        pred = model.predict(generator)
        label = np.argmax(pred[0])
        response['score'] = pred[0][label]

        detail = pd.read_csv(os.path.join(settings.BASE_DIR, 'category_detail', 'detail.csv'))
        response['name'] = detail['detail'][detail['code']==label].values[0]

        return render(request,'index.html',response)
    else:
        return render(request,'index.html')