import re

import utils


def tokenize(s):
    """
    Tokenize on parenthesis, punctuation, spaces and American units followed by a slash.

    We sometimes give American units and metric units for baking recipes. For example:
        * 2 tablespoons/30 milliliters milk or cream
        * 2 1/2 cups/300 grams all-purpose flour

    The recipe database only allows for one unit, and we want to use the American one.
    But we must split the text on "cups/" etc. in order to pick it up.
    """

    s = _expand_unit_abbreviations(s)
    s = _normalize_us_uk_split(s)

    return filter(None, re.split(r'([,\(\)])?\s*', utils.clumpFractions(s)))


def _expand_unit_abbreviations(s):
    s = re.sub(r'(\d+)g\.?', r'\1 grams', s)
    s = re.sub(r'(\d+)oz\.?', r'\1 ounces', s)
    s = re.sub(r'(\d+)lbs?\.?', r'\1 pounds', s)
    s = re.sub(r'(\d+)ml\.?', r'\1 milliliters', s)
    s = re.sub(r'(\d+)tsp\.?', r'\1 teaspoons', s)
    s = re.sub(r'(\d+)tbsp\.?', r'\1 tablespoons', s)
    return s


def _normalize_us_uk_split(s):
    american_units = [
        'cup', 'tablespoon', 'teaspoon', 'pound', 'ounce', 'quart', 'pint'
    ]
    for unit in american_units:
        s = s.replace(unit + '/', unit + ' ')
        s = s.replace(unit + 's/', unit + 's ')
    return s
