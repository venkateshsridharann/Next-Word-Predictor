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


def predict(request):
    input_text = ''
    if request.method == 'POST':
        input_text = request.POST['input_text']  # Get user input from the form

    token_list = tokenizer.texts_to_sequences([input_text])[0]
    token_list = pad_sequences([token_list], maxlen=model.input_shape[1], padding='pre')
    predicted = model.predict(token_list, verbose=0)[0]

    # Sort the predictions in descending order of probability
    sorted_indices = np.argsort(predicted)[::-1]
    
    # Get the top 3 predicted words and their probabilities
    top_words = []
    for index in sorted_indices[:3]:
        word = tokenizer.index_word[index]
        probability = predicted[index]
        top_words.append((word, probability))
    
    # Get the most probable word
    most_probable_word = top_words[0][0]
    predictions = top_words
    return render(request, 'prediction_results.html', {'input_text': input_text, 'predictions': predictions})    
