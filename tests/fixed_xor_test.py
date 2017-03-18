import unittest
from set1 import fixed_xor


class FixedXorUnitTest(unittest.TestCase):

    def setUp(self):
        self.buffer1 = "1c0111001f010100061a024b53535009181c"
        self.buffer2 = "686974207468652062756c6c277320657965"
        self.combination = "746865206b696420646f6e277420706c6179"


    def test_xor(self):
        result = fixed_xor.xor_combination(self.buffer1, self.buffer2)
        self.assertEqual(result, self.combination)
