import re

CMUDICT = 'cmudict.0.6-syl'
ALIGN   = 'm2m.input.m-mAlign.2-2.delX.1-best.conYX.align'

# ------------------
#  Helper functions
# ------------------

DIGITS = re.compile('\d')
def contains_digits(d):
    """Returns True if d contains any numeric characters"""
    return bool(DIGITS.search(d))

# ------------------
#  Key functions
# ------------------

def process_word_pronunciation(word, pronunciation):
    """Given an orthographic string, return a string of numbers 
       that represent whether the corresponding letter is in a syllable
       that has primary stress (1), secondary stress (2), 
       or is unstressed (0).
       
       Example: ABOLITIONIST -> A2.BO0.LI1.TION0.NIST0 -> 2001100000000"""
    pass
        

def make_dictionary():
    """Read CMUDICT and return dictionary of words (English orthography)
       and their stressed representation, including syllables and stress.
       Only use first pronunciation in case of multiple ones."""
    dictionary = dict()
    with open(CMUDICT, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('##'):
                continue
            if not line:
                continue
            word, pron = line.split('  ')
            if word.endswith(')'):
                continue
            if not word[0].isalpha():
                continue
            if contains_digits(word):
                continue
            # TODO: process orthographic and phonetic strings to match 
            #       letters/phones and bold the correct ones
            print ' '.join(list(word)), "\t", pron.replace('. ', '')\
                     .replace('0','').replace('1','').replace('2', '')
            
make_dictionary()
