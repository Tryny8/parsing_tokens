#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Classe TokenParser
"""


from parsing_tokens.build_parser.api_parser import (compile_single_token_matcher, compile_multiples_tokens_matcher,
                                                    parse_tokens, set_register_token_type, set_register_balise,
                                                    set_register_separator, get_register_all_token_type,
                                                    get_register_all_balise, get_register_all_separator)


class TokenParser:
    def __init__(self, content: str, *, segmentation="line", token_type="token", balise="bracket", separator="egale", type_display=True):
        self.content: str = content
        self.segmentation = segmentation
        self.current_balise = {"type_name": token_type, "balise_name": balise,
                               "separateur_name": separator, "type_display": type_display}
        self.patterns: list = []

        self._matcher = None
        self._registry_token_type = None
        self._registry_balise = None
        self._registry_separator = None

    def _build_single_matcher(self):
        if self._matcher is None:
            self._matcher = compile_single_token_matcher(self.current_balise["type_name"],
                                                         self.current_balise["balise_name"],
                                                         self.current_balise["separateur_name"],
                                                         self.current_balise["type_display"])

    def _build_multiple_matcher(self):
        """ {"type_name": 'token', "balise_name": 'bracket', "separateur_name": 'egale', "type_display": True}  """
        if len(self.patterns) < 2:
            raise ValueError("Please set at least 2 balises minimum !")
        if self._matcher is None:
            self._matcher = compile_multiples_tokens_matcher(self.patterns)

    def set_balise(self, balise, *, token_type="token", separator="egale", display_type=True):
        """ {"type_name": 'token', "balise_name": 'bracket', "separateur_name": 'egale', "type_display": True} """
        self.current_balise = {"type_name": token_type,
                          "balise_name": balise,
                          "separateur_name": separator,
                          "type_display": display_type}
        self.patterns.append(self.current_balise)
        self._matcher = None  # invalidate cache

    def reset_balise(self):
        self.patterns.clear()
        self._matcher = None  # invalidate cache

    def get_tokens(self, single_pattern=True, verbose=False):
        self._matcher = None  # invalidate cache
        if single_pattern:
            self._build_single_matcher()
        else:
            self._build_multiple_matcher()
        return parse_tokens(self.content, segmentation=self.segmentation, pattern=self._matcher, verbose=verbose)

    def get_all_balises(self) -> list:
        return self.patterns

    def add_token_type(self, name: str) -> None:
        set_register_token_type(name)

    def add_balise(self, name: str, open_char: str, close_char: str) -> None:
        set_register_balise(name, open_char=open_char, close_char=close_char)

    def add_separator(self, name: str, char: str) -> None:
        set_register_separator(name, char)

    def get_all_token_type(self) -> set[str]:
        self._registry_token_type: set[str] = get_register_all_token_type()
        return self._registry_token_type

    def get_all_balise(self) -> set[str]:
        self._registry_balise: set[str] = get_register_all_balise()
        return self._registry_balise

    def get_all_separator(self) -> set[str]:
        self._registry_separator: set[str] = get_register_all_separator()
        return self._registry_separator