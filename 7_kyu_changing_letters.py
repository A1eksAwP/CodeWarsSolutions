# https://www.codewars.com/kata/5831c204a31721e2ae000294

def swap(st):
    '''
    When provided with a String, capitalize all vowels
    For example:
    Input : "Hello World!"
    Output : "HEllO WOrld!"
    Note: Y is not a vowel in this kata.
    :param st:
    :return: str
    '''
    return ''.join(x.upper() if x in 'euioa' else x for x in st)
