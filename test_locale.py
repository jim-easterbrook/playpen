import locale
import os
import sys

print('setting locale')
os.environ['LANGUAGE'] = 'de_DE'
locale.setlocale(locale.LC_MESSAGES, '')

import exiv2

def main():
    str_en = str_en = 'Failed to read input data'
    print('translating')
    exiv2.ImageFactory.open(__file__)
    return 0

if __name__ == "__main__":
    sys.exit(main())
