#!/usr/bin/env python
# -*- coding: utf-8 -*-


def open_file(path: str) -> str:
    # API publique
    """
    Lit un fichier texte et retourne son contenu sous forme de str.

    r : mode lecture
    w : mode écriture (écrase tout)
    a : mode écriture (ajoute à la fin)
    """
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content