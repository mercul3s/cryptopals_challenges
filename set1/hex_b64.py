from sys import argv
from base64 import b64encode
from binascii import hexlify, unhexlify

"""
The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

"""

def tohex(string):
    return hexlify(string)

def dehex(hex_string):
    return unhexlify(hex_string)


def encode_string(raw_string):
    return b64encode(raw_string)


def main():
    if len(argv) > 1:
        encoded_arg = argv[1]
        return encode_string(dehex(encoded_arg))
    else:
        return "Please enter a hex string to encode in base64."


if __name__ == '__main__':
    main()
