import unittest

class TestLetterCounting(unittest.TestCase):

    def test_empty_string_has_zero_occurrences(self):
        from letters import vowel_frequency_consonant_sum
        self.assertEqual(dict(a=0, e=0, i=0, o=0, u=0, consonants=0), vowel_frequency_consonant_sum(''))

    def test_simple_vowel_counts(self):
        from letters import vowel_frequency_consonant_sum
        self.assertEqual(dict(a=0, e=1, i=2, o=3, u=4, consonants=0), vowel_frequency_consonant_sum('eiiooouuuu'))

    def test_case_independent_vowel_counts(self):
        from letters import vowel_frequency_consonant_sum
        self.assertEqual(dict(a=0, e=1, i=2, o=3, u=4, consonants=0), vowel_frequency_consonant_sum('eiIooOuuuU'))

    def test_simple_consonant_counting(self):
        from letters import vowel_frequency_consonant_sum
        self.assertEqual(dict(a=0, e=0, i=0, o=0, u=0, consonants=3), vowel_frequency_consonant_sum('bCd'))

    def test_counts_unaffected_by_extra_characters(self):
        from letters import vowel_frequency_consonant_sum
        self.assertEqual(dict(a=0, e=1, i=2, o=3, u=4, consonants=3),
                         vowel_frequency_consonant_sum('eiiooouuuu_+1234567890!@#$%^&*()bCd '))


if __name__ == '__main__':
    unittest.main()
