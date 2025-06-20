# src/word_picker.py
import random

def pick_word(words_by_level, level):
    return random.choice(words_by_level[level]).upper()
