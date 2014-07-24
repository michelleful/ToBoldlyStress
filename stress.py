"""
Given some text, return the stressed spelling version
"""
import re

BOLD_SINGLE_SYLLABLE = False

# Tricky parts: ignore commas, double quotes, etc while leaving 's alone
#               match the case in returning the stressed spelling

# use 'stressed_spelling.html' if you want secondary things to be italicised
STRESS_DICT_PATH = 'stressed_spelling.no_secondary.txt'
def load_dictionary():
    dictionary = dict()
    with open(STRESS_DICT_PATH, 'r') as f:
        for line in f:
            word, stressed_word = line.strip().split('\t')
            dictionary[word.strip()] = stressed_word.strip()
    return dictionary
    
STRESS_DICT = load_dictionary()

def process_word(word):
    """Look up stressed form of word, and perform various case manipulations
       etc."""
    if word.upper() not in STRESS_DICT:
        return word

    stressed = STRESS_DICT[word.upper()]

    # unbold single syllables
    if not BOLD_SINGLE_SYLLABLE:
        if stressed.startswith('<b>') and stressed.endswith('</b>'):
            return word

    if word.isupper():  # word is capitalized
        return stressed.upper().replace('B>','b>')
    elif word[0].islower():  # the whole word should be lower case
        return stressed.lower()
    else:
        return stressed  # sentence case is the default


# regular expression for extracting words

# originally had hyphen included but decided that left too many
# out-of-vocabulary words whose individual parts did have pronunciations.
# something to think about - compound stress?
word_re = re.compile(r"\b[A-Za-z']+\b")

def process_text(text):
    """Main function to be called in this module. Given some plain text
       return the text with primary-stressed syllables in bold.
       Bold is handled using HTML tags <b></b>"""
    return word_re.sub(lambda match: process_word(match.group()), text)
    


#print process_text("""Hello world! Look who's talking! IT'S ME!!!!! 
#                       He inexorably said about Aix-la-Chapelle.""")
