#!/usr/bin/env python
import locale
import random
import re
import sys
from copy import copy
from functools import partial
from optparse import OptionParser

EXIT_SUCCESS = 0
EXIT_ERROR = 1

punct_re = re.compile(r"(?!\w)(?!\s).")

DEFAULT_PASSWORD_COUNT = 1
DEFAULT_NUMBER_OF_WORDS = 4
DEFAULT_DICT_PATH = "/usr/share/dict/words"
DEFAULT_MIN = 4
DEFAULT_MAX = 6

EXCLUSIONS = [
    # (name, test)
    ("upper", lambda s: any(c for c in s if c.isupper())),
    ("numeric", lambda s: any(c for c in s if c.isdigit())),
    ("punct", lambda s: punct_re.search(s)),
    ]

def build_parser():
    parser = OptionParser()
    parser.add_option("-d", "--dict", "--dictionary",
        help="The default dictionary to use (default: %s)" % DEFAULT_DICT_PATH,
        action="store",
        dest="dictionary",
        metavar="PATH",
        default=DEFAULT_DICT_PATH,
        )
    parser.add_option("-c", "--count",
        help="The number of passwords to output (default: %i)" % DEFAULT_PASSWORD_COUNT,
        action="store",
        type="int",
        dest="count",
        default=DEFAULT_PASSWORD_COUNT,
        )
    parser.add_option("-i",
        help="The number of words to output (default: %i)" % DEFAULT_NUMBER_OF_WORDS,
        action="store",
        type="int",
        dest="length",
        default=DEFAULT_NUMBER_OF_WORDS,
        )
    parser.add_option("--min", "--min-len", "--min-length",
        help="The minimum length of word to consider (default: %i)" % DEFAULT_MIN,
        action="store",
        type="int",
        dest="min",
        default=DEFAULT_MIN,
        )
    parser.add_option("--max", "--max-len", "--max-length",
        help="The maximum length of word to consider (default: %i)" % DEFAULT_MAX,
        action="store",
        type="int",
        dest="max",
        default=DEFAULT_MAX,
        )
    for name, test in EXCLUSIONS:
        parser.add_option("--include-%s" % name,
            help="Include words containing %s chars" % name,
            action="store_true",
            default=False,
            dest=name,
            )
    parser.add_option("-v", "--verbose",
        help="Report additional statistics",
        action="store_true",
        dest="verbose",
        default=False,
        )
    return parser

def main():
    parser = build_parser()
    options, args = parser.parse_args()
    for test, desc in [
            (options.count < 1, "Count must be positive"),
            (options.length < 1, "Number of words must be positive"),
            (options.min < 1, "Minimum length must be positive"),
            (options.max < options.min, "Maximum length must not be less than the minimum"),
            ]:
        if test:
            sys.stderr.write("%s\n" % desc)
            parser.print_help()
            return EXIT_ERROR
    try:
        f = open(options.dictionary)
    except IOError:
        sys.stderr.write("Unable to open %s\n" % options.dictionary)
        return EXIT_ERROR
    else:
        try:
            word_list = []
            for word in f:
                word = word.rstrip() # get rid of the newline
                if options.min <= len(word) <= options.max:
                    # it's of the right length
                    for attr, exclusion_test in EXCLUSIONS:
                        if not getattr(options, attr):
                            if exclusion_test(word):
                                break
                    else:
                        word_list.append(word)
        finally:
            f.close()
        for i in range(options.count):
            result = " ".join(random.sample(word_list, options.length))
            print(result)
        if options.verbose:
            possibilities = len(word_list) ** options.length
            print("%i word dictionary, %i word(s) = %i possible" % (
                len(word_list),
                options.length,
                possibilities,
                ))
    return EXIT_SUCCESS

if __name__ == "__main__":
    sys.exit(main())
