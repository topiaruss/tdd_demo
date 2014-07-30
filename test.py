import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_empty_string_has_zero_occurrences(self):
        import letters
        self.assertEqual(dict(a=0, e=0, i=0, o=0, u=0), letters.vowel_frequency(''))

    def test_simple_vowel_counts(self):
        import letters
        self.assertEqual(dict(a=0, e=1, i=2, o=3, u=4), letters.vowel_frequency('eiiooouuu'))

if __name__ == '__main__':
    unittest.main()
