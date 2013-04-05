from libs.ply import lex
from settings.reserved_words import reserved_words
from settings.tokens import tokens
from settings.tokens_re import *
import os


class MJLex():
    """docstring for MJLex"""
    valid_tokens = True

    def __init__(self):
        self.valid_tokens = self.validateTokens("src/settings/tokens_re.py")

    def validateTokens(self, path):
        tokens_re_file = os.path.realpath(path)
        is_valid_tokens_re_file = lex._validate_file(tokens_re_file)
        if is_valid_tokens_re_file:
            # print tokens_re_file, "is good"
            return True
        else:
            # print tokens_re_file, "not is good"
            return False

    def MJLexer(self, input_file):
        """
        String input_file
        """
        if valid_tokens:
            print "\n-------MJCompiler-------\n\nby @MaoAiz & @edwinfmesa\n\n"
            a = lex.lex()
            a.input(input_file)
            print "Analyzing your code..."

            while True:
                try:
                    tok = a.token()
                    if not tok:
                        break  # No more input
                    print "\t", tok
                except Exception, e:
                    tok = "ERROR:", e
            print "analysis completed"
            return True
        else:
            print "Error 500, vuelve mas tarde"
        return False
