# Regural expression for tokens

# Operators
t_ADD = r'^\+$'		# Additive Operator. Olso used for String concatenation
t_SUB = r'^-$'		# Substraction Operator
t_MUL = r'^\*$'		# Multiplication Operator
t_DIV = r'^/$'		# Division Operator
t_RO = r'^%$'		# Remainder Operator
t_SAO = r'^=$'		# Simple Assignment Operator
t_LT = r'^<$'		# Less Than
t_LTE = r'^<=$'		# Less Than or Equal
t_GT = r'^>$'		# Greater Than
t_GTE = r'^>=$'		# Greater Than or Equal
t_ET = r'^==$'		# Equal to
t_NET = r'^!=$'		# Not Equal to
t_OR = r'^\|\|$'    # Conditional Or
t_AND = r'^&&$'		# Conditional And
t_UMO = r'^-$'		# Unary Minus Operator
t_LCO = r'^!$'		# Logical Complement Operator
# t_IDE = r'\w+'


def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("ValueError Exception: %d", t.value)
        t.value = 0
    return t


def t_HEX(t):
    r'\d+'
    try:
        t.value = hex(t.value)
    except ValueError:
        print("ValueError Exception: %d", t.value)
        t.value = 0
    return t


def t_IDE(t):
    r'[a-zA-Z_]{1}\w+'
    t.value = t.value[:20]
    return t


def t_NL(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    return t


def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)
