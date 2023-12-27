import locale
import os
import sys

##print('setting locale')
##os.environ['LANGUAGE'] = 'de_DE'
##locale.setlocale(locale.LC_MESSAGES, '')

import exiv2

def main():
    print('untranslated')
    try:
        exiv2.ImageFactory.open(__file__)
    except exiv2.Exiv2Error as ex:
        print(str(ex))
    print('setting locale')
    os.environ['LANGUAGE'] = 'de_DE'
    locale.setlocale(locale.LC_MESSAGES, '')
    print('translated')
    try:
        exiv2.ImageFactory.open(__file__)
    except exiv2.Exiv2Error as ex:
        print(str(ex))
    return 0

if __name__ == "__main__":
    sys.exit(main())
