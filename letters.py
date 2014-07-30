def vowel_frequency(s):
    """return dict of vowel frequency
       assumes ASCII only.
       TODO: refine spec and requirements re: i18n.
    """
    stats = {}
    for v in 'aeiou':
        stats[v] = s.count(v)
    return stats