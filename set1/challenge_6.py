import challenge_3
"""
Break repeating-key XOR
It is officially on, now.
This challenge isn't conceptually hard, but it involves actual error-prone coding. The other challenges in this set are there to bring you up to speed. This one is there to qualify you. If you can do this one, you're probably just fine up to Set 6.

There's a file here. It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:
this is a test
and
wokka wokka!!!
is 37. Make sure your code agrees before you proceed.

For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.

The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.

Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
Solve each block as if it was single-character XOR. You already have code to do this.
For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.
This code is going to turn out to be surprisingly useful later on. Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing. But more people "know how" to break it than can actually break it, and a similar technique breaks something much more important.

No, that's not a mistake.
We get more tech support questions for this challenge than any of the other ones. We promise, there aren't any blatant errors in this text. In particular: the "wokka wokka!!!" edit distance really is 37.
"""


def normalized_hamming(keysize, filename):
    """
    Takes an int (keysize) and a file handler, and computes 
    the hamming distance of 4 sequential blocks of length keysize
    from the file. Returns a normalized hamming distance value as a int.
    """

    blocks = []
    distances = []
    for num in range(4):
        blocks.append(filename.read(keysize))

    for i, val in enumerate(blocks):
        while len(distances) <= 3:
            hamm_dist = hamming(blocks[i], blocks[i + 1])
            distances.append(hamm_dist)

    hamming_norm = sum(distances) / len(distances)
    return hamming_norm


def hamming(string1, string2):
    """
    Computes the hamming distance (bit # difference)
    of two equal length strings. Returns an int.
    For binary strings a and b the Hamming distance is
    equal to the number of ones (population count)
    in a XOR b. 
    """

    if len(string1) == len(string2):
        counter = 0
        for i in range(0, len(string1)):
            diff = format(ord(string1[i]) ^ ord(string2[i]), 'b')
            # print "XOR diff is {}".format(diff)
            for d in diff:
                if int(d) > 0:
                    counter += int(d)
        return counter
    return "Error: string length unequal"


def cipher_block(keysize, ciphertext):
    """
    Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
    """
    # iterate over ciphertext
    # take keysize number of bytes from text
    # append that to the blocklist
    text = ciphertext.read()
    block_list = []
    for i in range(0, len(text), keysize):
        block_list.append(text[i:i + keysize])
    return block_list


def transpose_cipher(keysize, block_list):
    """
    Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
    """
    transposed_block_list = []   
    for i in range(keysize):
        transposed_block_list.append("".join(block[i] for block in block_list))
    return transposed_block_list


def solve_xor(transposed_block_list):
    """
    Solve each block as if it was single-character XOR. You already have code to do this.
    For each block, the single-byte XOR key that produces the best looking histogram 
    is the repeating-key XOR key byte for that block. Put them together and you have the key.
    """
    for block in transposed_block_list:
        print block
        solutions = challenge_3.decrypt(block)
        print solutions

def main():
    keys_and_hamming_distance_dict = {}
    for key_len in range(2, 41):
        f = open("set1/challenge_6_data.txt", 'r')
        normalized_dist = normalized_hamming(key_len, f)
        keys_and_hamming_distance_dict[key_len] = normalized_dist
        f.close()
    potential_key_lengths = sorted(keys_and_hamming_distance_dict.iteritems(), key=lambda (k, v): (v, k))[0:3]
    print potential_key_lengths

if __name__ == '__main__':
    main()
