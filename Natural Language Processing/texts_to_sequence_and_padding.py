# -*- coding: utf-8 -*-
"""texts_to_sequence_and_padding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k0H409HXlr48eHfufyVTmD7ZUBSt0dCw
"""

import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
             'i love my cat',
             'I love my car',
             'You love your dog!',
             'Do you have a car?',
             'Do you think my cat is amazing?'
]

tokenizer = Tokenizer(num_words = 100, oov_token="<OOV>") #100개의 words를 저장할 수 있는 tokenizer 생성
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)

sequences = tokenizer.texts_to_sequences(sentences)

padded = pad_sequences(sequences, maxlen = 5)

print("\nSequences = " , sequences)
print("\nPadded Sequences:")
print(padded)

test_data = [
             'i really love my dog',
             'my cat loves my house'
]

test_seq = tokenizer.texts_to_sequences(test_data)
print("\nTest sequence = ", test_seq)

padded = pad_sequences(test_seq, maxlen=10)
print("\nPadded Test Sequence: ")
print(padded)

