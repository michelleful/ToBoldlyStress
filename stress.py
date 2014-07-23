"""
Given some text, return the stressed spelling version
"""
import re

# Tricky parts: ignore commas, double quotes, etc while leaving 's alone
#               match the case in returning the stressed spelling

# use 'stressed_spelling.html' if you want secondary things to be italicised
STRESS_DICT_PATH = 'stressed_spelling.no_secondary.txt'
def load_dictionary():
    dictionary = dict()
    with open(STRESS_DICT_PATH, 'r') as f:
        for line in f:
            word, stressed_word = line.strip().split('\t')
            dictionary[word.strip()] = stressed_word
    return dictionary
    
STRESS_DICT = load_dictionary()
        
word_re = re.compile(r"\b[A-Za-z']+\b")

def process_word(word):
    # TODO: match case
    return STRESS_DICT[word.upper()]

def process_text(text):
    return word_re.sub(lambda match: process_word(match.group()), text)
    

