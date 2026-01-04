# parsing-tokens [v0.2.0]

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