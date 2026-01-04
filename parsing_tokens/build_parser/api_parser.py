#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
API TokenParser
"""


import re
from re import Pattern
from collections.abc import Iterable, Iterator

from parsing_tokens.build_parser.core_parser import (_build_token_pattern_str, _build_token_pattern_str_without_name,
                                                     _is_invalid_type_name_str, _is_invalid_balise_name_str,
                                                     _is_invalid_separateur_name_str, _build_balise_name_str,
                                                     _build_separateur_name_str, _compile_single_pattern,
                                                     _merge_token_patterns, _register_balise_chars,
                                                     _register_separator_char)
from parsing_tokens.build_parser.register_parser import (TOKEN_TYPES, BALISE_TYPES, SEPARATORS,
                                                         BALISE_MAP, SEPARATOR_MAP)
from parsing_tokens.build_segmentation.api_segmentation import segment_content


#-----------------------------------------------------------------------------------------------------------------------
def create_token_pattern(type_name: str = "token", balise_name: str = "bracket", separateur_name: str = "egale",
                         type_display: bool = True) -> str:
    # API publique
    """
    Crée un pattern regex pour identifier un token balisé.
        Format avec type : [type=nom]
    type_display à True → BALISE TYPE SÉPARATEUR NOM_TYPE BALISE
        Format sans type : [nom]
    type_display à False → BALISE NOM_TYPE BALISE

    :param type_name: le type (à choisir dans une liste de la doc)
    :param balise_name: un str de la balise : crochet parenthèse ou bracket
    :param separateur_name: un str du séparateur : égale ou deux points
    :param type_display: un bool si on a le nom du type dans le texte
    :return:
    """
    test = False
    if type_name == "token" and test:
        print("LOG - Pattern : Attention nom du type non-définie !")
    if balise_name == "bracket" and test:
        print("LOG - Pattern : Attention nom de la balise non-définie !")
    if separateur_name == "egale" and test:
        print("LOG - Pattern : Attention nom du séparateur non-définie !")

    if _is_invalid_type_name_str(type_name):
        raise ValueError(f"Type de token non-accepté : {type_name}")
    if _is_invalid_balise_name_str(balise_name):
        raise ValueError(f"Type de balise non-accepté : {balise_name}")
    if _is_invalid_separateur_name_str(separateur_name):
        raise ValueError(f"Type de séparateur non-accepté : {separateur_name}")

    pre_balise, post_balise = _build_balise_name_str(balise_name)
    separateur = _build_separateur_name_str(separateur_name)

    if type_display:
        patt_test: str = _build_token_pattern_str(type_name, separateur, pre_balise, post_balise)
        # print(patt_test)
        return patt_test
    else:
        pattern_test: str = _build_token_pattern_str_without_name(pre_balise, post_balise)
        # print(patt_test)
        return pattern_test


#-----------------------------------------------------------------------------------------------------------------------
def compile_single_token_matcher(token_type: str, balise: str, separator: str, type_display: bool) -> Pattern[str]:
    # API publique
    """ Implémentation erronée, mais fonctionnel → ne pas créer de pattern dans cette fonction """
    pattern: str = create_token_pattern(token_type, balise, separator, type_display=type_display)
    return _compile_single_pattern(pattern)


def compile_multiples_tokens_matcher() -> Pattern[str]:
    # API publique
    """ Implémentation erronée, mais fonctionnel → ne pas créer de pattern dans cette fonction """
    pattern_1 = create_token_pattern('token', 'bracket', 'egale')
    pattern_2 = create_token_pattern('ast', 'parenthese', 'deux_points')
    pattern_3 = create_token_pattern(balise_name='bracket', type_display=False)
    pattern_4 = create_token_pattern('interpreter', 'crochet', 'egale')
    return _merge_token_patterns([pattern_1, pattern_2, pattern_3, pattern_4])

#-----------------------------------------------------------------------------------------------------------------------
def generator_tokens_in_line(line: str, pattern: Pattern[str]) -> Iterator[str]:
    # API publique
    for token in iter_tokens_in_line(line, pattern):
        yield token


def iter_tokens_in_line(line: str, pattern: Pattern[str]) -> Iterator[str]:
    # API publique
    for match in re.findall(pattern, line):
        yield match


def extract_tokens(contenu_units: Iterable[tuple[int, str]], pattern: Pattern[str], verbose: bool):
    # API publique
    tokens_by_unit: dict[int, list[str]] = {}
    for line_number, line in contenu_units:
        for token in generator_tokens_in_line(line, pattern):
            tokens_by_unit.setdefault(line_number, []).append(token)
            if verbose:
                print(f"Pattern found in line {line_number}: {token}")
    return tokens_by_unit


def parse_tokens(content: str, *, segmentation="line", pattern: Pattern[str] | None = None, verbose=False):
    # API publique
    if pattern is None:
        raise ValueError("pattern must be provided")
    units: Iterable[tuple[int, str]] = segment_content(content, segmentation)
    return extract_tokens(units, pattern, verbose)


#-----------------------------------------------------------------------------------------------------------------------
def set_register_token_type(name: str) -> None:
    # API publique
    """Ajoute un nouveau type de token."""
    if not isinstance(name, str) or not name:
        raise ValueError("token type must be a non-empty string")
    TOKEN_TYPES.add(name)


def set_register_balise(name: str, *, open_char: str, close_char: str) -> None:
    # API publique
    """Ajoute une nouvelle balise."""
    BALISE_TYPES.add(name)
    _register_balise_chars(name, open_char, close_char)


def set_register_separator(name: str, char: str) -> None:
    # API publique
    """Ajoute un nouveau séparateur."""
    SEPARATORS.add(name)
    _register_separator_char(name, char)


def get_register_all_token_type() -> set:
    # API publique
    """Retourne les types de token."""
    return TOKEN_TYPES


def get_register_all_balise() -> set:
    # API publique
    """Retourne les balises."""
    return BALISE_TYPES


def get_register_all_separator() -> set:
    # API publique
    """Retourne les séparateurs."""
    return SEPARATORS