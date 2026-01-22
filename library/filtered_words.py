"""
This program will filter the file and save five-letter words to different file. It also doesn't copy
words with polish characters.
"""

with open("slowa.txt", 'r', encoding='utf-8') as r, \
    open("slowa_piecioliterowe.txt", 'a', encoding="utf-8") as w:

    five_letter_words = []
    polish_characters = ["ą", "ć", "ę", "ł", "ń", "ó", "ś", "ź", "ż"]

    for word in r:
        word = word.strip().upper()
        if len(word) == 5:
            if word.isalpha() and word.isascii():
                w.write(word + "\n")


