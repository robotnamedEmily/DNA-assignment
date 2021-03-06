def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1) > len(dna2):
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    occurrences = 0
    for letter in dna:
        if letter == nucleotide:
            occurrences += 1
    return occurrences


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
    else:
        return False
        
def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if dna only contains the letters 'A', 'C', 'G', 
    or 'T'.

    >>>is_valid_sequence('ACTGAAGT')
    True
    >>>is_valid_sequence('AGTVCT')
    False

    """
    valid = 0
    for letter in dna:
        if letter not in 'ACGT':
            valid += 1
    if valid > 0:
        return False
    else: 
        return True
        
def insert_sequence(dna1, dna2, indx):
    """ (str, str, int) -> str

    Return the string produced by inserting dna2 at the index of dna1 provided 
    by indx.

    >>>insert_sequence('ACTGTA', 'CCC', 3)
    'ACTCCCGTA'
    >>>insert_sequence('GTTACTCA', 'ACGT', -1)
    'GTTACTCACGTA'

    """

    return dna1[:indx] + dna2 + dna1[indx:]
    
def get_complement(nucleotide):
    """(str) -> str

    Return the complement for the nucleotide provided.

    >>>get_complement('A')
    T
    >>>get_complement('C')
    G
    >>>get_complement('G')
    C
    >>>get_complement('T')
    A

    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    else:
        return 'A'

def get_complementary_sequence(dna):
    """(str) -> str

    Return the sequence that is complementary to the sequence 
    provided.

    >>>get_complementary_sequence('AAGCTATTG')
    TTCGATAAC
    >>>get_complementary_sequence('GTCTAAGG')
    CAGATTCC
    >>>get_complementary_sequence('TCAGTC')
    AGTCAG

    """
    complementary_sequence = ''
    for nucleotide in dna:
        if nucleotide == 'A':
            complementary_sequence += 'T'
        elif nucleotide == 'C':
            complementary_sequence += 'G'
        elif nucleotide == 'G':
            complementary_sequence += 'C'
        else:
            complementary_sequence += 'A'
    return complementary_sequence