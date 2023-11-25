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
# tokenizer.save_pretrained("./mlfiles/gpt2_tokenizer")
# model.save_pretrained("./mlfiles/gpt2_model")


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

def get_next_word_probabilities_2(sentence, top_k=3):

    def _predict_(input_text):
        print(input_text)
        input_text = input_text.strip()
        inputs = tokenizer.encode(input_text, return_tensors="tf")
        with tf.device("/CPU:0"):  # Ensure CPU usage for inference
            predictions = model(inputs).logits
            return predictions

    # Get the model predictions for the sentence.
    predictions = _predict_(sentence)

    # Get the next token candidates.
    next_token_candidates_tensor = predictions[0, -1, :]

    # Get the top k next token candidates.
    topk_candidates_indexes = tf.argsort(next_token_candidates_tensor, direction='DESCENDING')[:top_k]
    topk_candidates_indexes = tf.sort(topk_candidates_indexes)  # Sort for consistent results

    # Get the token probabilities for all candidates.
    all_candidates_probabilities = tf.nn.softmax(next_token_candidates_tensor, axis=-1)

    # Filter the token probabilities for the top k candidates.
    topk_candidates_probabilities = tf.gather(all_candidates_probabilities, topk_candidates_indexes).numpy()

    # Decode the top k candidates back to words.
    topk_candidates_tokens = [
        tokenizer.decode([idx]).strip() for idx in topk_candidates_indexes]

    # Return the top k candidates and their probabilities as a list of tuples.
    return list(zip(topk_candidates_tokens, topk_candidates_probabilities))

def predict_2(sentence):
    sentence = sentence.strip()
# Get the top k candidates and their probabilities
    top_k_candidates = get_next_word_probabilities_2(sentence, 3)
    # Print the top k candidates and their probabilities
    output = {}
    for candidate, probability in top_k_candidates:
        output[probability.round(2)] = {'word': candidate, 'probability': str(probability.round(2))}
    output = dict(sorted(output.items(),reverse=True))
    return list(output.values())


# AJAX handling funtion returning output from server to frontend as Json
@csrf_exempt
def ajax_view(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        response_list = predict_2(text) 
        print(response_list)
        return JsonResponse({'response_text': response_list})
    
# ==========================================================
# OLDER PREDICTION FUNCTION (NO PROBABILITY)
# ==========================================================
# def predict(input_text):
#     print(input_text)
#     input_text = input_text.strip()
#     output_texts = []
#     input_ids = tokenizer.encode(input_text, return_tensors="tf")
#     l = input_ids.shape[1]
#     # Generate text using the model
#     attention_mask = tf.ones(input_ids.shape, dtype=tf.int32)
#     output = model.generate(input_ids, 
#                                 max_length=l+1, 
#                                 num_return_sequences=3, 
#                                 no_repeat_ngram_size=1, 
#                                 num_beams=3, 
#                                 attention_mask=attention_mask)
        
#     # Decode and print the generated text
#     generated_texts = [clean(tokenizer.decode(seq, skip_special_tokens=True),input_text) for seq in output]
#     print(generated_texts)
#     return str(generated_texts)
# ==========================================================


# ==========================================================
# TEST PREDICTION FUNCTION WITH RUNTIME
# ==========================================================
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
# ==========================================================



