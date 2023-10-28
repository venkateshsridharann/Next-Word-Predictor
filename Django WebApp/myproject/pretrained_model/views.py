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
from transformers import pipeline, set_seed
# bert-base-cased and gpt2 using pipeline
# from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

# Create a view for the input form for rendering '/predict' 
def input_form(request):
    return render(request, 'prediction_results.html')

def clean(inp,input_text):
    inp = inp.replace("/","").replace("\t"," ").replace("\n","").replace("\\","").replace("_","").replace(input_text,"").strip()
    inp = inp.replace("\xa0"," ").replace("】","").replace("【","")
    return inp

def predict(input_text):
    print(input_text)
    l = len(input_text.split(' '))
    out = generator(input_text, max_length=l+20, num_return_sequences=3)

    out = [clean(x['generated_text'],input_text) for x in out]
    out = [[x,x.split()[0]] for x in out]
    print(out)
    return out
# function that uses bert-base-cased
# def predict(input_text):
#     print(input_text)
#     unmasker = pipeline('fill-mask', model='bert-base-cased')
#     out = unmasker(input_text+'[MASK]' )
#     out = list(set([x['token_str'] for x in out]))
#     print(out)
#     return out


# AJAX handling funtion returning output from server to frontend as Json
@csrf_exempt
def ajax_view(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        response_text = predict(text) 
        print(response_text)
        return JsonResponse({'response_text': str(response_text)})