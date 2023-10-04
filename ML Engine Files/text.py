import pandas as pd
import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

medium_data = pd.read_csv('medium_data.csv')
medium_data.describe()

medium_data['title'] = medium_data['title'].apply(lambda x: x.replace(u'\xa0',u' '))
medium_data['title'] = medium_data['title'].apply(lambda x: x.replace('\u200a',' '))

tokenizer = Tokenizer(oov_token='<oov>') # For those words which are not found in word_index
tokenizer.fit_on_texts(medium_data['title'])
total_words = len(tokenizer.word_index) + 1

input_sequences = []
for line in medium_data['title']:
    token_list = tokenizer.texts_to_sequences([line])[0]
    #print(token_list)
    
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))
input_sequences[1]

model = keras.models.load_model("next_word_try_2.keras") 


list_input = ["will AI become"]

def predictor(input):
    next_words = 1
    for seed_text in list_input:
        for _ in range(next_words):
            token_list = tokenizer.texts_to_sequences([seed_text])[0]
            token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')

            # Predict probabilities for all words
            predicted_probabilities = model.predict(token_list, verbose=0)[0]

            # Get the indices of the top 3 predicted words
            top3_word_indices = np.argsort(predicted_probabilities)[-3:][::-1]

            # Get the top 3 words and their probabilities
            top3_words = [tokenizer.index_word[idx] for idx in top3_word_indices]
            top3_probabilities = [round(predicted_probabilities[idx],3) for idx in top3_word_indices]
            print(seed_text)
            for i in range(len(top3_words)):
                o = str(top3_words[i])+" ("+str(top3_probabilities[i])+")"
                print(o)
                        
    #         # Print the top 3 suggestions
    #         print("Top 3 Predictions:")
    #         for word, prob in zip(top3_words, top3_probabilities):
    #             print(f"{word}: {prob:.4f}")

            # Choose the word with the highest probability as the next word
            output_word = top3_words[0]
            seed_text += " " + output_word
        print(seed_text)
            

predictor(list_input)