#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
from re import Pattern
from parsing_tokens.build_parser.register_parser import (TOKEN_TYPES, BALISE_TYPES, SEPARATORS,
                                                         BALISE_MAP, SEPARATOR_MAP)


#-----------------------------------------------------------------------------------------------------------------------
def _compile_single_pattern(pattern: str) -> Pattern[str]:
    # Bas niveau
    """ Regex complie => format : pattern """
    return re.compile(pattern)


def _merge_token_patterns(patterns: list[str]) -> Pattern[str]:
    # Bas niveau
    """ Regex complie => format : pattern_1 + "|" + pattern_2 + "|" + pattern_3 + "|" + pattern_4 """
    return re.compile("|".join(f"(?:{p})" for p in patterns))


#-----------------------------------------------------------------------------------------------------------------------
def _build_token_pattern_str(name: str, separateur: str, pre_balise: str, post_balise: str) -> str:
    # Bas niveau
    """ Regex pattern => format : [type=nom du type] """
    return (rf"{pre_balise}" +                  # BALISE
            rf"{name}" +                        # TYPE
            rf"{separateur}" +                  # SÉPARATEUR
            rf"[^{separateur}{post_balise}]+" + # NOM_TYPE
            rf"{post_balise}")                  # BALISE


def _build_token_pattern_str_without_name(pre_balise: str, post_balise: str) -> str:
    # Bas niveau
    """ Regex pattern => format : [nom du type] """
    return (rf"{pre_balise}" +                  # BALISE
            rf"[^{post_balise}]+" +             # NOM_TYPE
            rf"{post_balise}")                  # BALISE


#-----------------------------------------------------------------------------------------------------------------------
def _is_invalid_type_name_str(type_name: str) -> bool:
    # Bas niveau
    """ Choix du type pris en charge par la fonction regex """
    return type_name not in TOKEN_TYPES


def _is_invalid_balise_name_str(balise_name: str) -> bool:
    # Bas niveau
    """ Choix de la balise pris en charge par la fonction regex """
    return balise_name not in BALISE_TYPES


def _is_invalid_separateur_name_str(separateur_name: str) -> bool:
    # Bas niveau
    """ Choix du séparateur pris en charge par la fonction regex """
    return separateur_name not in SEPARATORS


#-----------------------------------------------------------------------------------------------------------------------
def _build_balise_name_str(balise_name: str) -> tuple[str, str]:
    # Bas niveau
    """ Choix de la balise pris en charge par la fonction regex: Registre BALISE_MAP"""
    try:
        return BALISE_MAP[balise_name]
    except KeyError:
        raise ValueError(f"Unknown balise name : {balise_name}")


def _build_separateur_name_str(separateur_name: str) -> str:
    # Bas niveau
    """ Choix du séparateur pris en charge par la fonction regex: Registre SEPARATOR_MAP """
    try:
        return SEPARATOR_MAP[separateur_name]
    except KeyError:
        raise ValueError(f"Unknown separateur name : {separateur_name}")