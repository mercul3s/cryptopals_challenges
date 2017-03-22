from binascii import hexlify
"""
Implement repeating-key XOR
Here is the opening stanza of an important work of the English language:

Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal

Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

It should come out to:

0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.
"""

def encrypt(key, text):
    """
    Takes a key(string), text(string) and returns a hex
    encoded string XOR encrypted against the key.
    """

    # split the string into chunks based on the size of the key
    # zip chunks, call xor fun
    # if there are any remaining chars in the string,
    # split the key based on the size of remaining chars
    # finally, hex encode and return
    result = ""
    for i in range(0, len(text), len(key)):
        
        zipped = zip(key, text[i:(i + len(key))])
        result += "".join(char_xor(k, t) for k, t in zipped)
        print "Text is {}, result is {}".format(text[i:(i + len(key))], result)

    return hex_encode(result)


def split_text(key_length, text):
    pass


def hex_encode(text):
    """
    Encodes a text string to hex using binascii lib.
    """
    return hexlify(text)


def char_xor(key_char, text_char):
    """
    Returns the char value of the XORed ordinal of two chars.
    """
    return chr(ord(key_char) ^ ord(text_char))
