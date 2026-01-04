#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Main TokenParser
"""


from re import Pattern

from parsing_tokens.build_io.api_io import open_file
from parsing_tokens.build_parser.api_parser import compile_hardcoded_tokens_matcher, parse_tokens


def main(verbose=False):
    contenu = open_file("data_test/test.txt")

    pattern: Pattern[str] = compile_hardcoded_tokens_matcher()  # type: ignore

    if verbose:
        print("<<Start of File>>")

    tokens_by_line = parse_tokens(contenu, segmentation="line", pattern=pattern, verbose=verbose)

    if verbose:
        print("<<End of File>>")

    print("All Tokens Main:", tokens_by_line)


if __name__ == "__main__":
    main()