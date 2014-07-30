import re

VOWELS = 'aeiou'
CONS = 'bcdfghjklmnpqrstvwxyz'
CONS_RE = re.compile("[%s]" % CONS)

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

    stats['consonants'] = len(CONS_RE.findall(s))

    return stats