from sys import argv
from base64 import b64encode
from binascii import unhexlify

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
