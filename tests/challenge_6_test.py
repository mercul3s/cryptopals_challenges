import unittest
from set1 import challenge_6

class HammingDistanceTest(unittest.TestCase):

    def setUp(self):
        self.string1          = "this is a test"
        self.string2          = "wokka wokka!!!"
        self.hamming_distance = 37

    # def test_hamming(self):
    #     result = challenge_6.hamming(self.string1, self.string2)
    #     self.assertEqual(result, self.hamming_distance)
