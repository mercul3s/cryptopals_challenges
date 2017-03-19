import unittest
from set1 import challenge_3


class Challenge3UnitTest(unittest.TestCase):
    
    def setUp(self):
        self.hex_encoded_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        self.decrypted_string = "Cooking MC's like a pound of bacon"

    def test_decrypt(self):
        result = challenge_3.decrypt(self.hex_encoded_string)
        self.assertEqual(result, self.decrypted_string)
