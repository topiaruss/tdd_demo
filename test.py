import unittest

class TestLetterCounting(unittest.TestCase):

    def test_empty_string_has_zero_occurrences(self):
        import letters
        self.assertEqual(dict(a=0, e=0, i=0, o=0, u=0), letters.vowel_frequency(''))

    def test_simple_vowel_counts(self):
        import letters
        self.assertEqual(dict(a=0, e=1, i=2, o=3, u=4), letters.vowel_frequency('eiiooouuuu'))

    def test_counts_unaffected_by_other_characters(self):
        import letters
        self.assertEqual(dict(a=0, e=1, i=2, o=3, u=4), letters.vowel_frequency('eiiooouuuu_+1234567890!@#$%^&*()bcd'))

    def test_simple_consonant_counting(self):
        import letters
        self.assertEqual(dict(a=0, e=0, i=0, o=0, u=0, consonants=1), letters.vowel_frequency('b'))

if __name__ == '__main__':
    unittest.main()
