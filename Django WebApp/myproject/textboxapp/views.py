from django.shortcuts import render
from django.http import HttpResponse
import os
import keras
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model


# Load the machine learning model and data
model = keras.models.load_model('mlfiles/next_word_try_2.keras')

with open('mlfiles/tokenizer.pickle', 'rb') as file:
    tokenizer = pickle.load(file)

def textbox_page(request):
    return render(request, 'textboxapp/textbox.html')

