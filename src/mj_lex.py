from libs.ply import lex
from settings.reserved_words import reserved_words
from settings.tokens import tokens
from settings.tokens_re import *
import os

tokens_re_file = os.path.realpath("src/settings/tokens_re.py")
is_valid_tokens_re_file = lex._validate_file(tokens_re_file)
if is_valid_tokens_re_file:
    print tokens_re_file, "is good"
else:
    print tokens_re_file, "not is good"
