from binascii import unhexlify
import collections
import string
"""
Single-byte XOR cipher
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

Achievement Unlocked
You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.
"""

alphabet = string.lowercase + string.uppercase
encoded_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
freqs_english = {
                    'a': 8.167, 
                    'b':1.492, 
                    'c':2.782, 
                    'd':4.253, 
                    'e':12.702, 
                    'f':2.228, 
                    'g':2.015, 
                    'h':6.094, 
                    'i':6.966,
                    'j':0.153, 
                    'k':0.772, 
                    'l':4.025, 
                    'm':2.406, 
                    'n':6.749, 
                    'o':7.507, 
                    'p':1.929, 
                    'q':0.095, 
                    'r':5.987, 
                    's':6.327, 
                    't':9.056,
                    'u':2.758, 
                    'v':0.978, 
                    'w':2.360, 
                    'x':0.150, 
                    'y':1.974, 
                    'z':0.074
                }


def decrypt(char, hex_string):
    result = ""
    for l in hex_string:
        result += (chr(ord(char) ^ ord(l)))
    return result


# determine character frequency of a string and return
# the most frequenly occurring character
# note: this returns the lowercase x, which decodes the 
# unhexed string as 'cOOKINGmcSLIKEAPOUNDOFBACON'.
# close, but not quite; the actual XOR'd char is uppercase X.
def score(raw_string):
    frequency_percent = collections.defaultdict(int) 
    frequency_map = collections.defaultdict(int)
    for char in raw_string:
        frequency_map[char] = frequency_map.get(char, 0) + 1
    
    for i in string.printable:
        frequency_percent[i] = 100 * float(frequency_map[i])/float(len(raw_string))

    frequency_score = 0
    diffkeys = [k for k in freqs_english if freqs_english[k] != frequency_percent[k]]
    for k in diffkeys:
        # print k, ':', freqs_english[k], '->', frequency_percent[k]
        frequency_score += abs((freqs_english[k] - frequency_percent[k]))
    # print "Overall frequency score: {}".format(frequency_score)
    return frequency_score

    # # sort the dict by value
    # freq_sort = sorted(frequency_map.iteritems(), key=lambda (k,v): (v, k))
    # print freq_sort
    # # grab the char in the last tuple in the list (highest value char)
    # return freq_sort[-1]


def main():
    dehexed = unhexlify(encoded_string)
    for letter in alphabet:
        decoded = decrypt(letter, dehexed)
        f_score = score(decoded)
        if f_score < 80.0:
            print "Letter is {}, decoded string is {}, frequency score is {}\n".format(letter, decoded, f_score)

if __name__ == '__main__':
    main()
