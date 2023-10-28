import os
import keras
import pickle
import numpy as np
import tensorflow as tf
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from tensorflow.keras.models import load_model
from django.views.decorators.csrf import csrf_exempt
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from transformers import pipeline, set_seed


# bert-base-cased and gpt2 can also use the 'pipeline'
# from transformers import pipeline
# generator = pipeline('text-generation', model='gpt2')

# # Load and save the pre-trained GPT-2 model and tokenizer
# model = TFGPT2LMHeadModel.from_pretrained("gpt2")
# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# tokenizer.save_pretrained("../mlfiles/gpt2_tokenizer")
# model.save_pretrained("../mlfiles/gpt2_model")


# Load the tokenizer and model 
tokenizer = GPT2Tokenizer.from_pretrained("./mlfiles/gpt2_tokenizer")
model = TFGPT2LMHeadModel.from_pretrained("./mlfiles/gpt2_model")

# Create a view for the input form for rendering '/predict' 
def input_form(request):
    return render(request, 'prediction_results.html')

def clean(inp,input_text=''):
    inp = inp.replace("/","").replace("\t"," ").replace("\n","").replace("\\","").replace("_","").replace(input_text,"").strip()
    inp = inp.replace("\xa0","").replace("】","").replace("【","")
    return inp

def predict(input_text):
    print(input_text)
    input_text = input_text.strip()
    output_texts = []
    input_ids = tokenizer.encode(input_text, return_tensors="tf")
    l = input_ids.shape[1]
    # Generate text using the model
    attention_mask = tf.ones(input_ids.shape, dtype=tf.int32)
    output = model.generate(input_ids, 
                                max_length=l+1, 
                                num_return_sequences=3, 
                                no_repeat_ngram_size=1, 
                                num_beams=3, 
                                attention_mask=attention_mask)
        
    # Decode and print the generated text
    generated_texts = [clean(tokenizer.decode(seq, skip_special_tokens=True),input_text) for seq in output]
    print(generated_texts)
    return str(generated_texts)

# AJAX handling funtion returning output from server to frontend as Json
@csrf_exempt
def ajax_view(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        response_text = predict(text) 
        print(response_text)
        return JsonResponse({'response_text': str(response_text)})
    



# import time
# def test():
#     start_time = time.time()
#     input_texts = ["There are two purpose-built options to manage ", "this seems to"]

#     for input_ in input_texts:
#         input_text = input_.strip()
#         input_ids = tokenizer.encode(input_text, return_tensors="tf")
#         l = input_ids.shape[1]
#         # attention helps predictions stay relevant 
#         attention_mask = tf.ones(input_ids.shape, dtype=tf.int32)
#         # Generate text using the model
#         output = model.generate(input_ids, 
#                                 max_length=l+1, 
#                                 num_return_sequences=3, 
#                                 no_repeat_ngram_size=1, 
#                                 num_beams=3, 
#                                 attention_mask=attention_mask)
#         # Decode and print the generated text
#         generated_texts = [clean(tokenizer.decode(seq, skip_special_tokens=True)) for seq in output]
#         print(generated_texts)
#         print('\n')
#     end_time = time.time()
#     runtime = end_time - start_time
#     print("Runtime predict : {:.2f} seconds".format(runtime))
