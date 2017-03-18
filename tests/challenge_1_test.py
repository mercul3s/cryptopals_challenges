import unittest
from set1 import challenge_1 

class HexB64UnitTest(unittest.TestCase):


    def setUp(self):
        self.hexed_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        self.unhexed_string = "I'm killing your brain like a poisonous mushroom"
        self.b64_encoded_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


    def test_dehex(self):
        unhexed_string = challenge_1.dehex(self.hexed_string)
        self.assertEqual(unhexed_string, self.unhexed_string)


    def test_encode_string(self):
        encoded_string = challenge_1.encode_string(self.unhexed_string)
        self.assertEqual(encoded_string, self.b64_encoded_string)
