#!/usr/bin/env python
# -*- coding: utf-8 -*-


TOKEN_TYPES = {"token", "ast", "interpreter"}
BALISE_TYPES = {"parenthese", "bracket", "crochet"}
SEPARATORS = {"deux_points", "egale"}
BALISE_MAP = {
    "parenthese": (r"\(", r"\)"),
    "bracket": (r"\[", r"\]"),
    "crochet": (r"\{", r"\}")
}
SEPARATOR_MAP = {
    "egale": "=",
    "deux_points": ":"
}