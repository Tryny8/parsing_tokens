#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections.abc import Iterable, Iterator

from parsing_tokens.build_segmentation.core_segmentation import split_lines, split_blocks


def generator_line(text: str) -> Iterator[tuple[int, str]]:
    # API publique
    for line_number, line in enumerate(split_lines(text), start=1):
        yield line_number, line


def generator_block(text: str) -> Iterator[tuple[int, str]]:
    # API publique
    for index, block in enumerate(split_blocks(text), start=1):
        yield index, block


def segment_content(content: str, type_segmentation: str) -> Iterable[tuple[int, str]]:
    # API publique
    if type_segmentation == "line":
        return generator_line(content)
    elif type_segmentation == "block":
        return generator_block(content)
    else:
        raise ValueError("Unknown segmentation")