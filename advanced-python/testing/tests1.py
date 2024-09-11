import unittest 

from prime import is_prime

class Tests(unittest.TestCase):

    def test_1(self):
        """Check that 1 is not prime """
        self.assertFalse(is_prime(1))

    def test_2(self):
        """Check that 2 is not prime """
        self.assertFalse(is_prime(2))

    def test_5(self):
        """Check that 5 is prime """
        self.assertTrue(is_prime(5))

    def test_10(self):
        """Check that 10 is not prime """
        self.assertFalse(is_prime(10))

    def test_11(self):
        """Check that 11 is prime """
        self.assertTrue(is_prime(11))

    def test_16(self):
        """Check that 16 is not prime """
        self.assertFalse(is_prime(16))

    def test_25(self):
        """Check that 25 is not prime """
        self.assertFalse(is_prime(25))

    def test_30(self):
        """Check that 30 is not prime """
        self.assertFalse(is_prime(30))

if __name__ == "__main__":
    unittest.main()
