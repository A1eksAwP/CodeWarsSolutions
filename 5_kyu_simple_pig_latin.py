# https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):
    """ Move the first letter of each word to the end of it,
    then add "ay" to the end of the word. Leave punctuation marks untouched.
    Examples:
    func: pig_it('Pig latin is cool') -> igPay atinlay siay oolcay
    func: pig_it('Hello world !') -> elloHay orldway ! """
    return ' '.join([f'{ch[1:]}{ch[:1]}ay' if ch.isalpha() else ch for ch in text.split()])
