#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Classe TokenParser
"""


import re

from parsing_tokens.parser import TokenParser
from parsing_tokens.build_io.api_io import open_file
from parsing_tokens.build_parser.api_parser import set_register_token_type, create_token_pattern


def test_custom_token_type():
    set_register_token_type("custom")
    pattern = create_token_pattern("custom", "bracket", "egale")
    assert re.findall(pattern, "[custom=hello]")


def test_default_token_still_works():
    pattern = create_token_pattern("token", "bracket", "egale")
    assert re.findall(pattern, "[token=test]")


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

    parser.add_token_type("task")
    parser.add_balise("chevron", open_char="<", close_char=">")
    parser.add_separator("tiret", "-")

    print(parser.get_all_token_type())
    print(parser.get_all_balise())
    print(parser.get_all_separator())


    test_custom_token_type()
    test_default_token_still_works()


if __name__ == "__main__":
    main()