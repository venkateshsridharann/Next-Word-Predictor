import os
import keras
import pickle
import numpy as np
import tensorflow as tf
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import JsonResponse
from tensorflow.keras.models import load_model
from django.views.decorators.csrf import csrf_exempt
from tensorflow.keras.preprocessing.sequence import pad_sequences



# Load the machine learning model and data
model = keras.models.load_model('mlfiles/custom_next_word_try_2.keras')

with open('mlfiles/custom_tokenizer.pickle', 'rb') as file:
    tokenizer = pickle.load(file)

# Create a view for rendering the root (dummy)'' 
def textbox_page(request):
    return render(request, 'textbox.html')


# Create a view for the input form for rendering '/predict' 
def input_form(request):
    return render(request, 'prediction_results.html')

# function that takes input tokenizedwords and returns output from ML Model
def predict(input_text):
    print(input_text)
    token_list = tokenizer.texts_to_sequences([input_text])[0]
    token_list = pad_sequences([token_list], maxlen=model.input_shape[1], padding='pre')
    predicted = model.predict(token_list, verbose=0)[0]

    # Sort the predictions in descending order of probability
    sorted_indices = np.argsort(predicted)[::-1]
    
    # Get the top 3 predicted words and their probabilities
    output = {}
    for index in sorted_indices[:3]:
        word = tokenizer.index_word[index]
        probability = predicted[index]
        output[probability.round(2)]= {'word': word, 'probability': str(probability.round(2))}
    output = dict(sorted(output.items(),reverse=True))
    return list(output.values()) 

# AJAX handling funtion returning output from server to frontend as Json
@csrf_exempt
def ajax_view(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        response_list = predict(text) 
        print(response_list)
        return JsonResponse({'response_text': response_list})