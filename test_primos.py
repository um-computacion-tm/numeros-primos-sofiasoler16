import unittest

from primos import is_primo


class TestPrimos(unittest.TestCase):
    
    def test_primos(self):
        result = is_primo(7)
        self.assertTrue(result)
    def test_no_primos(self):
        result = is_primo(8)
        self.assertFalse(result)
    def test_no_primos2(self):
        result = is_primo(177)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()