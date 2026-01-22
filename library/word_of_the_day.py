import random

list_of_words = []
FILE_NAME = 'library/slowa_piecioliterowe.txt'

def word_draw():
    with open(FILE_NAME, "r", encoding='utf-8') as f:
        for word in f:
            list_of_words.append(word.strip().upper())

        word_to_guess = random.choice(list_of_words)
        return word_to_guess, list_of_words
