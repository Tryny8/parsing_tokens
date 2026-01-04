#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Classe TokenParser
"""


from parsing_tokens.build_parser.api_parser import (compile_single_token_matcher, parse_tokens,
                                                    set_register_token_type, set_register_balise,
                                                    set_register_separator, get_register_all_token_type,
                                                    get_register_all_balise, get_register_all_separator)


class TokenParser:
    def __init__(self, content: str, *, segmentation="line", token_type="token", balise="bracket", separator="egale", type_display=True):
        self.content: str = content
        self.segmentation = segmentation
        self.token_type = token_type
        self.balise = balise
        self.separator = separator
        self.type_display = type_display

        self._matcher = None
        self._registry_token_type = None
        self._registry_balise = None
        self._registry_separator = None

    def _build_matcher(self):
        if self._matcher is None:
            self._matcher = compile_single_token_matcher(self.token_type, self.balise, self.separator,
                                                         self.type_display)

    def set_balise(self, balise, *, token_type=None, separator=None):
        # Evolution possible en :
        # configure_token()
        # set_token_format()
        self.balise = balise
        if token_type is not None:
            self.token_type = token_type
        if separator is not None:
            self.separator = separator
        self._matcher = None  # invalidate cache

    def get_tokens(self, verbose=False):
        self._build_matcher()
        return parse_tokens(self.content, segmentation=self.segmentation, pattern=self._matcher, verbose=verbose)

    def add_token_type(self, name: str) -> None:
        set_register_token_type(name)

    def add_balise(self, name: str, open_char: str, close_char: str) -> None:
        set_register_balise(name, open_char=open_char, close_char=close_char)

    def add_separator(self, name: str, char: str) -> None:
        set_register_separator(name, char)

    def get_all_token_type(self) -> set:
        self._registry_token_type = get_register_all_token_type()
        return self._registry_token_type

    def get_all_balise(self) -> set:
        self._registry_balise = get_register_all_balise()
        return self._registry_balise

    def get_all_separator(self) -> set:
        self._registry_separator = get_register_all_separator()
        return self._registry_separator