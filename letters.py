import re

VOWELS = 'aeiou'
CONS = 'bcdfghjklmnpqrstvwxyz'

def vowel_frequency_consonant_sum(s):
    """return dict of vowel frequency and sum of all consonants
       assumes ASCII only.
       assumes case independent.
       TODO: check spec and requirements re: i18n and case
    """
    s = s.lower()

    stats = {}

    for v in VOWELS:
        stats[v] = s.count(v)

    cons_re = re.compile("[%s]" % CONS)
    stats['consonants'] = len(cons_re.findall(s))

    return stats