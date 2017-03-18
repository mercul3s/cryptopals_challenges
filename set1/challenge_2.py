from challenge_1 import dehex, tohex
from sys import argv

"""

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179

"""

def xor_combination(hex1, hex2):

    if len(hex1) != len(hex2):
        raise "Error: hex strings are not equal length."

    string1 = dehex(hex1)
    string2 = dehex(hex2)

    # combine the letters of each string in sequence
    # so each can be compared numerically (char ordinal)
    # zipped is a list of tuples; x and y are first and 
    # second elements in each tuple.
    zipped = zip(string1, string2)
    
    result = "".join(chr(ord(x) ^ ord(y)) for x, y in zipped)

    return tohex(result)


def main():
    if len(argv) > 1:
        encoded_arg1 = argv[1]
        encoded_arg2 = argv[2]
        return xor_combination(encoded_arg1, encoded_arg2)
    else:
        return "Please enter two hex strings to combine."

if __name__ == '__main__':
    main()
