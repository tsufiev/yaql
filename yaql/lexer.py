import ply.lex as lex

keywords = {
    'true': 'TRUE',
    'false': 'FALSE',
    'null': 'NULL'
}

keywords_to_val = {
    'TRUE': True,
    'FALSE': False,
    'NULL': None
}

tokens = [
    'SYMBOL',
    'STRING',
    'QUOTED_STRING',
    'NUMBER',
    'FUNC',
    'GE',
    'LE',
    'NE',
    'FILTER',
    'TUPLE',
    'OR',
    'AND',
    'NOT',
    'IS',
    'DOLLAR'
] + list(keywords.values())

literals = "+-*/.()]><=,"

t_ignore = ' \t'


t_GE = '>='
t_LE = '<='
t_NE = '!='

t_TUPLE = '=>'


def t_SYMBOL(t):
    """
    \\b\\w+\\:\\w+\\b
    """
    return t


def t_DOLLAR(t):
    """
    \\$\\d*
    """
    return t


def t_AND(t):
    """
    \\band\\b
    """
    return t


def t_OR(t):
    """
    \\bor\\b
    """
    return t


def t_NOT(t):
    """
    \\bnot\\b
    """
    return t


def t_IS(t):
    """
    \\bis\\b
    """
    return t


def t_NUMBER(t):
    """
    \\b\\d+(\\.?\\d+)?\\b
    """
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t


def t_FUNC(t):
    """
    \\b\\w+\\(
    """
    t.value = t.value[:-1]
    return t

#  (?<=\\w)\\[|(?<=\\])\\[|(?<=\\$)\\[


def t_FILTER(t):
    """
   (?<!\\s)\\[
    """
    return t


def t_STRING(t):
    """
    \\b\\w+\\b
    """
    t.type = keywords.get(t.value, 'STRING')
    t.value = keywords_to_val.get(t.type, t.value)
    return t


def t_QUOTED_STRING(t):
    """
    '(?:[^'\\\\]|\\\\.)*'
    """
    t.value = t.value[1:-1].replace('\\', '')

    return t


def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)


lexer = lex.lex()