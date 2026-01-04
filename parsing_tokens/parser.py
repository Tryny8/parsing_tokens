#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Classe TokenParser
"""


from parsing_tokens.build_parser.api_parser import compile_single_token_matcher, parse_tokens


class TokenParser:
    def __init__(self, content: str, *, segmentation="line", token_type="token", balise="bracket", separator="egale", type_display=True):
        self.content: str = content
        self.segmentation = segmentation
        self.token_type = token_type
        self.balise = balise
        self.separator = separator
        self.type_display = type_display

        self._matcher = None

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