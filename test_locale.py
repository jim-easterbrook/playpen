import locale
import sys

import exiv2

def main():
    str_en = str_en = 'Failed to read input data'
    print('setting locale')
    locale.setlocale(locale.LC_MESSAGES, 'de_DE')
    print('translating')
    exiv2.ImageFactory.open(__file__)
    return 0

if __name__ == "__main__":
    sys.exit(main())
