import unittest
from set1 import challenge_5


class RepeatingXorUnitTest(unittest.TestCase):

    def setUp(self):
        self.cleartext = "Burning 'em, if you ain't quick and nimble\n" \
                          "I go crazy when I hear a cymbal"
        self.encrypted = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272" \
                          "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
        self.key = "ICE"

    # def test_encryption(self):
    #     result = challenge_5.encrypt(self.key, self.cleartext)
    #     self.assertEqual(result, self.encrypted)

    def test_char_xor(self):
        result = challenge_5.char_xor('a', 'b')
        self.assertEqual(result, '\x03')

    def test_decryption(self):
        result = challenge_5.decrypt(self.key, self.encrypted)
        self.assertEqual(result, self.cleartext)
