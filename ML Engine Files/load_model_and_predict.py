import os
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # '2' to suppress information and warnings, only display error messages
tf.get_logger().setLevel('ERROR')  # Suppress TensorFlow warnings as well

# Load the saved tokenizer
with open("tokenizer.pickle", "rb") as handle:
    tokenizer = pickle.load(handle)

# Load the saved model
model = load_model("next_word_try_2.keras")

# Function to predict the next three words with their probabilities
def predict(input_text):
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
    
    return top_words, most_probable_word

# Example usage:
input_text = input("Input text here :")
input_text = input_text.strip()
print('\n'+input_text+'\n')
predictions, most_probable_word = predict(input_text)
for word, probability in predictions:
    print("{} ({})".format(word, str(probability.round(2))))
print("\n{} {}".format(input_text, most_probable_word))
