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

def align(orthographic_alignment, phonetic_alignment):
    """Returns a list of tuples of corresponding indices between
       an aligned orthographic string and an aligned phonetic string.
       Phonetic index FIRST
       
       Example: A|B|O|L|I|T:I|O|N|        AE|B|AH|L|IH|SH|AH|N|
                -> [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,7),(7,8)]
    """
    index_pairs = list()
    phonetic_index = 0
    orthographic_index = 0
    for phon, ortho in zip(phonetic_alignment.split('|'), 
                           orthographic_alignment.split('|')):
        index_pairs.append((phonetic_index, orthographic_index))
        if phon == '_':
            pass
        else:
            phonetic_index += len(phon.split(':'))
        if ortho == '_':
            pass
        else:
            orthographic_index += len(ortho.split(':'))
    return index_pairs[:-1]

def process_word_pronunciation(word, pronunciation):
    """Given an orthographic string, return a list of tuples
       representing (start_index_of_syllable, stress_type_of_syllable)
       stress_type is represented by 1 = primary stress, 2 = secondary stress,
       0 = zero stress.

       Example: ABOLITIONIST -> A2.BO0.LI1.TIO0.NIST0
                             -> [(0,2), (1,0), (3,1), (5,0), (8,0)]
    """
    pass



def process_dictionary():
    """Read CMUDICT and return dictionary of words (English orthography)
       to a list of tuples representing 
       (start_index_of_syllable, stress_type_of_syllable) where phones are
       the entities indexed over.
       
       Example: ABOLITIONIST -> AE2 . B AH0 . L IH1 . SH AH0 . N AH0 S T
                             -> [(0,2), (1,0), (3,1), (5,0), (8,0)]

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

#            dictionary[word] = 

#            print ' '.join(list(word)), "\t", pron.replace('. ', '')\
#                     .replace('0','').replace('1','').replace('2', '')
    return dictionary
            
process_dictionary()

def process_aligned_data():
    """Read in the aligned data and return a dictionary of words to 
       their syllabified *orthographic* strings"""
    pass
