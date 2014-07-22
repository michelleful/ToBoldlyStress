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
       Phonetic index FIRST, to the index of the *last* character of the
       corresponding orthographic substring
       
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
            for i in range(len(phon.split(':'))):
                phonetic_index += 1
                index_pairs.append((phonetic_index, orthographic_index))
        if ortho == '_':
            pass
        else:
            orthographic_index += len(ortho.split(':'))
    index_pairs.append((len(phonetic_alignment), len(orthographic_alignment)))
    return index_pairs


def stressed_representation(orthographic_string, phonetic_string, 
                            alignment_dict):
    """Given three ingredients: the orthographic representation of a word,
       its pronunciation (CMU dict representation), and a dictionary of
       index alignments, return a stressed representation of the *orthography*.
       <1></1> around the primary-stressed syllable, 
       <2></2> around the secondary-stressed syllables,
       <0></0> around the unstressed syllables
    """
    # zeroth, let's convert the orthographic string into sentence case
    # for easier reading
    orthographic_string = orthographic_string.capitalize()

    # first, process the phonetic string to determine the ENDING indices
    # of each syllable and the stress value
    phon_indices = list()
    end_index = 0
    for syllable in phonetic_string.split('.'):
        syllable = syllable.strip()
        end_index += len(syllable.split(' '))
        syllable = syllable.strip()
        phon_indices.append((end_index, DIGITS.findall(syllable)[0]))

    # convert the phonetic indices to orthographic indices using
    # the alignment dictionary
    ortho_indices = [(alignment_dict[phon_index], syllable_stress)
                      for phon_index, syllable_stress in phon_indices]

    # now insert <n></n> around each syllable for appropriate value of n
    stressed_string = ""
    prev_index = 0
    for ortho_index, syllable_stress in ortho_indices:
        stressed_string += "<%s>" % syllable_stress + \
                           orthographic_string[prev_index:ortho_index] + \
                           "</%s>" % syllable_stress
        prev_index = ortho_index

    return stressed_string

        
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
            # eliminate abbreviations and things like "HMM",
            # which have no stress repr anyway
            if not contains_digits(pron):
                continue

            if word in ALIGNMENTS:
                dictionary[word] = stressed_representation(word, pron, 
                                                           ALIGNMENTS[word])
    return dictionary
         
# --------------
#    MAIN
# --------------
            
STRESS_DICT = process_dictionary()

for word, stressed_spelling in sorted(STRESS_DICT.items()):
    print stressed_spelling.replace('<1>','<b>').replace('</1>','</b>')\
                           .replace('<2>','<em>').replace('</2>','</em>')\
                           .replace('<0>','').replace('</0>','')
