#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections.abc import Iterable


def split_lines(text: str) -> Iterable[str]:
    # Bas niveau
    return text.splitlines()


def split_blocks(text: str) -> Iterable[str]:
    # Bas niveau
    # TODO : future logique
    return [text]