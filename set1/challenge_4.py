from sys import argv
import challenge_3
import string

"""
Detect single-character XOR
One of the 60-character strings in this file http://cryptopals.com/static/challenge-data/4.txt has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
"""

# This prints out all potential matches, including the encoded
# string - for better matching, run the decoded strings though
# the scoring algorithm again and output the lowest scoring
# match.
# Decoded text: 'Now that the party is jumping' against XOR 5
# Encoded string: '7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f'
def check_encrypted_text(filename):
    f = open(filename, 'r')
    result = None
    for line in f:
        line = line.strip("\n")
        if len(line) % 2 == 0:
            result = challenge_3.decrypt(line)

            if all(c in string.printable for c in result[1]):
                print "Encoded text is {}".format(line)
                print "Decoded text is {}".format(result[1])
                print "XOR char is {}\n".format(result[0])


def main():
    if len(argv) > 1:
        check_encrypted_text(argv[1])
        
    else:
        print "Please enter a filename."

if __name__ == '__main__':
    main()
