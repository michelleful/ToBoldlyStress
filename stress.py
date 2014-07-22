
CMUDICT = 'cmudict.0.6-syl'

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
            # TODO: process orthographic and phonetic strings to match 
            #       letters/phones and bold the correct ones
            
get_dictionary()
