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


def stressed_representation(orthographic_string, phonetic_string, 
                            alignment_dict):
    """Given three ingredients: the orthographic representation of a word,
       its pronunciation (CMU dict representation), and a dictionary of
       index alignments, return a stressed representation of the *orthography*.
       <1></1> around the primary-stressed syllable, 
       <2></2> around the secondary-stressed syllables,
       <0></0> around the unstressed syllables
    """
    pass

# ------------------
#  File processing 
# ------------------

def process_aligned_data():
    """Read in the aligned data and return a dictionary of words to a dictionary
       of alignments (the result of align(ortho, pron))"""
    dictionary = dict()
    with open(ALIGN, 'r') as f:
        for line in f:
            ortho, pron = line.split('\t')
            word = ''.join(ortho.split('|')).replace(':','').replace('_','')
            dictionary[word] = dict(align(ortho, pron))
    return dictionary

ALIGNMENTS = process_aligned_data()

def process_dictionary():
    """Read CMUDICT and return dictionary of words (English orthography)
       to a list of tuples representing 
       (start_index_of_syllable, stress_type_of_syllable) where graphemes are
       the entities indexed over.
       
       Example: ABOLITIONIST -> A2.BO0.LI1.TIO0.NIST0
                             -> [(0,2), (1,0), (3,1), (5,0), (8,0)]

       Only use first pronunciation in case of multiple ones.
    """

    dictionary = dict()
    with open(CMUDICT, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('##'):
                continue
            if not line:
                continue
            word, pron = line.split('  ')

            # filter out duplicates, punctuation marks and words with numbers
            if word.endswith(')'):
                continue
            if not word[0].isalpha():
                continue
            if contains_digits(word):
                continue

            # TODO

    return dictionary
            
STRESS_DICT = process_dictionary()


