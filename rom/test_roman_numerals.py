from .rom import rom

BASIC_NUMS = ['i', 'ii', 'iii', 'iv', 'v',
              'vi', 'vii', 'viii', 'ix', 'x',
              'xi', 'xii', 'xiii', 'xiv', 'xv',
              'xvi', 'xvii', 'xviii', 'xix', 'xx']

SCATTER_NUMS = {
    'c': 100,
    'cd': 400,
    'CDVI': 406,
    'LIV': 54,
    'mmix': 2009
}


def test_parse_basic_count():
    for i in range(len(BASIC_NUMS)):
        assert int(rom(BASIC_NUMS[i])) == i + 1


def test_parse_scatter():
    for k, v in SCATTER_NUMS.items():
        assert int(rom(k)) == v


def test_generate_basic_count():
    for i in range(len(BASIC_NUMS)):
        assert str(rom(i + 1)) == BASIC_NUMS[i].upper()


def test_generate_scatter_count():
    for k, v in SCATTER_NUMS.items():
        assert str(rom(v)) == k.upper()
