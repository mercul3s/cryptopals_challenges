import unittest
from set1 import challenge_6

class HammingDistanceTest(unittest.TestCase):

    def setUp(self):
        self.string1          = "this is a test"
        self.string2          = "wokka wokka!!!"
        self.hamming_distance = 37

    def test_hamming(self):
        result = challenge_6.hamming(self.string1, self.string2)
        self.assertEqual(result, self.hamming_distance)

    def test_normalized_hamming(self):
        f = open("set1/challenge_6_data.txt", 'r')
        result = challenge_6.normalized_hamming(4, f)
        self.assertEqual(result, 12)
