# parsing-tokens [v0.3.0]

Librairie Python de tokenisation de texte basée sur des patterns regex.

⚠️ Projet en cours de développement  
API susceptible d’évoluer.

## Installation
pip install git+https://github.com/Tryny8/parsing_tokens.git

## Usage rapide
```python
from parsing_tokens import TokenParser
from parsing_tokens.build_io.api_io import open_file

content = open_file("data_test/test.txt")
parser = TokenParser(content)
# Exemple de balise customs nommée
parser.set_balise("parenthese", token_type='ast', separator='deux_points')
# Exemple de balise customs nommée
parser.set_balise("bracket", token_type='token', separator='egale')
# Retourne un dictionnaire avec tous les tokens
tokens = parser.get_tokens()
```

## ⚠️ Version 0.3.0 – Important Changes API

Starting from v0.3.0, multiple token patterns are no longer hardcoded.
Users must now explicitly define token patterns using dictionaries.

Example:

```python
from parsing_tokens.build_parser.api_parser import compile_multiples_tokens_matcher

patterns = [
    {"type_name": "token", "balise_name": "bracket", "separateur_name": "egale", "type_display": True},
    {"type_name": "ast", "balise_name": "parenthese", "separateur_name": "deux_points", "type_display": True},
]

matcher = compile_multiples_tokens_matcher(patterns)
```