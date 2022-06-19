import roman

valid_list = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII')

def is_valid(numeral):
    return numeral in valid_list

def from_roman(numeral):
    if not is_valid(numeral):
        raise ValueError("{numeral} is not in accepted list of values: {', '.join(valid_list)")
    return roman.fromRoman(numeral)

def to_roman(number):
    return roman.toRoman(number)
