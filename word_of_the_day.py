import random

list_of_words = []

def word_draw():
    with open('slowa_piecioliterowe.txt', "r", encoding='utf-8') as f:
        for word in f:
            list_of_words.append(word)

        word = random.choice(list_of_words)
        return word
