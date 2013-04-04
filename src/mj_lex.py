from libs.ply import lex
from settings.reserved_words import reserved_words
from settings.tokens import tokens
from settings.tokens_re import *
import os

# print lex
tokens_re_file =  os.path.realpath("src/tokens_re.py")
print lex._validate_file(tokens_re_file)
# print tokens
# print "SUMA", t_ADD
