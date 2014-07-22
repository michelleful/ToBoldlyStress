"""
Given some text, return the stressed spelling version
"""
import re

# Tricky parts: ignore commas, double quotes, etc while leaving 's alone
#               match the case in returning the stressed spelling

#word_re = re.compile(r"?\b[0-9A-Za-z']+\b'?")

STRESS_DICT_PATH = 'stressed_spelling.no_secondary.txt'
def load_dictionary():
    dictionary = dict()
    with open(STRESS_DICT_PATH, 'r') as f:
        for line in f:
            word, stressed_word = line.split('\t')
            dictionary[word] = stressed_word
    return dictionary
    
STRESS_DICT = load_dictionary()
        

