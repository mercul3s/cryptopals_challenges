from sys import argv
import challenge_3

"""
Detect single-character XOR
One of the 60-character strings in this file http://cryptopals.com/static/challenge-data/4.txt has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
"""

# lots of non printable characters
def check_encrypted_text(filename):
    f = open(filename, 'r')

    for line in f:
        line = line.strip("\n")
        if len(line) % 2 == 0:
            result = challenge_3.decrypt(line)
            print "Encoded text is {} and decoded result is {}".format(line, result)


def main():
    if len(argv) > 1:
        check_encrypted_text(argv[1])
    else:
        return "Please enter a filename."

if __name__ == '__main__':
    main()
