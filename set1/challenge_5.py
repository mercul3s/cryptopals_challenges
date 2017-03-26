from binascii import hexlify, unhexlify
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
    result = split_text(key, text)
    return hexlify(result)

def decrypt(key, encrypted_text):
    """
    Takes a hex-encoded, XORed string and returns
    decoded plain text.
    """
    hex_removed = unhexlify(encrypted_text)
    result = split_text(key, hex_removed)
    return result


# Should be able to do this as a recursive function. Think about
# the way Elixir and Clojure loop over sets of data - head | tail
# and recur the tail.
def split_text(key, text):
    result = ""
    for i in range(0, len(text), len(key)):
        zipped = zip(key, text[i:(i + len(key))])
        result += "".join(char_xor(k, t) for k, t in zipped)
    return result


def char_xor(key_char, text_char):
    """
    Returns the char value of the XORed ordinal of two chars.
    """
    return chr(ord(key_char) ^ ord(text_char))
