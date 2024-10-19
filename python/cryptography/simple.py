"""
There are two types of encryption:
one that will prevent your sister from reading your diary
and one that will prevent your government.
~ Bruce Schneier
"""

def xor(str, key):
    """
    xor cipher
    """
    result = ""
    length = len(str)
    i,j = 0,0
    while i < length:
        result += chr(ord(str[i]) ^ ord(key[j]))
        i += 1
        j += 1
        if j == len(key):
            j = 0
    return result


def ascii(str, offset=255):
    """
    ascii offset cipher
    to decipher just run again
    """
    result = ""
    for char in str:
        result += chr(offset - ord(char))
    return result
