#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Classe TokenParser
"""
import sys
print(sys.path)

from parsing_tokens.parser import TokenParser
from parsing_tokens.build_io.api_io import open_file


def main(verbose=False):
    content = open_file("data_test/test.txt")
    parser = TokenParser(content)

    parser.set_balise("bracket")
    tokens = parser.get_tokens()

    for line, value in tokens.items():
        print(">>", line, value, value[0].strip("[]").split("="))

    print("All Tokens bracket:", tokens)

    parser.set_balise("parenthese", token_type='ast', separator='deux_points')
    tokens = parser.get_tokens(verbose=verbose)

    for line, value in tokens.items():
        print(">>", line, value, value[0].strip("()").split(":"))

    print("All Tokens parenthese:", tokens)


if __name__ == "__main__":
    main()