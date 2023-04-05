# https://www.codewars.com/kata/52223df9e8f98c7aa7000062

"""
How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:

"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"
"""
import re


def re_rot13(msg):
    return ''.join(chr(ord(ch) + 13) if re.match(r'[a-mA-M]', ch) else chr(ord(ch) - 13) if re.match(r'[n-zN-Z]', ch) else ch for ch in msg)


def easter_egg_rot13(msg):
    return msg.encode('rot13')


def seq_rot13(msg):
    ENC = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DEC = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    return ''.join(DEC[ENC.find(ch)] if ch.isalpha() else ch for ch in msg)
