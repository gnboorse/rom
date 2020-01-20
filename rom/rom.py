
from collections import deque
# roman numeral symbols and their values
SYMBOL_TABLE = {
    'i': 1,
    'v': 5,
    'x': 10,
    'l': 50,
    'c': 100,
    'd': 500,
    'm': 1000
}

# largest number that can be represented by traditional roman numerals
SYMBOL_TABLE_ORDERED = sorted(
    list(SYMBOL_TABLE.items()), key=lambda x: x[1], reverse=True)
MAX_NUMBER = 3999


def rom(val, **kwargs):
    return RomanNumeral(val, **kwargs)


class RomanNumeral:
    '''
    class representing a roman numeral.
    contains a string representation (i.e. xvii)
    and an integer representation (i.e. 17)
    '''
    str_val = None
    int_val = None

    def __init__(self, value, **kwargs):
        if isinstance(value, int):
            self.int_val = value
            self.str_val = rom_generate(value, **kwargs)
        elif isinstance(value, str):
            self.int_val = rom_parse(value.lower())
            self.str_val = rom_generate(self.int_val, **kwargs)
        elif isinstance(value, RomanNumeral):
            self.str_val = value.str_val
            self.int_val = value.int_val
        else:
            raise TypeError(
                "Value must be an int, str, or another roman numeral")

    def __str__(self):
        return self.str_val

    def __repr__(self):
        return self.str_val

    def __int__(self):
        return self.int_val


def rom_parse(val):
    '''parse from string to numeric'''
    val = val.lower().strip()
    if val == 'n':
        return 0
    running_sum = 0
    largest_place = 0
    previous_vals = deque(maxlen=3)
    for i in range(-1, -1*(len(val)+1), -1):
        # iterate from right to left
        c = val[i]
        # get numeric value assigned to this character
        numeric_val = SYMBOL_TABLE.get(c)
        if not numeric_val:
            # raise exception if invalid character provided
            raise ValueError('Unable to parse invalid roman numeral "' +
                             val + '", found illegal character "' + c + '"')

        if len(previous_vals) == 3 and all(n == c for n in previous_vals):
            # this is now the 4th matching character in a row
            raise ValueError(
                'Unable to parse invalid roman numeral "' + val +
                '", found more than 3 repeating instances of "' + c + '" in a row')

        if len(previous_vals) > 0:
            most_recent = SYMBOL_TABLE.get(previous_vals[-1])
            if most_recent <= numeric_val:
                running_sum += numeric_val
                if numeric_val > largest_place:
                    largest_place = numeric_val
                elif numeric_val < largest_place:
                    raise ValueError('Unable to parse invalid roman numeral "' +
                                     val + '", invalid ordering. Irregular subtractive notation not allowed.')
            else:  # most_recent > numeric_val
                running_sum -= numeric_val
        else:
            running_sum += numeric_val
            largest_place = numeric_val
        previous_vals.append(c)  # always appened to deque when done
    return running_sum


def rom_generate(val, caps=True):
    '''produce string from numeric'''
    if val > MAX_NUMBER:
        raise ValueError(
            "Unable to generate roman numeral. Value larger than max value.")
    if val == 0:
        return 'N' if caps else 'n'
    num_str = ''
    remainder = val
    for i in range(len(SYMBOL_TABLE_ORDERED)):
        k, v = SYMBOL_TABLE_ORDERED[i]
        division = remainder // v
        if division > 0:  # additive notation (easy path)
            num_str += k * division
            remainder = remainder % v
         # now consider case where we need to generate with subtractive notation
        offset = None
        if str(v)[0] == '5' and i < len(SYMBOL_TABLE_ORDERED) - 1:
            offset = 1
        elif str(v)[0] == '1' and i < len(SYMBOL_TABLE_ORDERED) - 2:
            offset = 2

        if offset is not None:
            k1, v1 = SYMBOL_TABLE_ORDERED[i + offset]
            if remainder >= (v - v1):
                num_str += k1 + k
                remainder -= (v - v1)

    return num_str.upper() if caps else num_str.lower()
