import string

from django.template.defaultfilters import safe

from django import template
register = template.Library()

__all__ = ['tel']

ALPHANUM = string.digits + string.ascii_uppercase

DIGIT_MAP = {
    u'A' : u'2',
    u'B' : u'2',
    u'C' : u'2',
    u'D' : u'3',
    u'E' : u'3',
    u'F' : u'3',
    u'G' : u'4',
    u'H' : u'4',
    u'I' : u'4',
    u'J' : u'5',
    u'K' : u'5',
    u'L' : u'5',
    u'M' : u'6',
    u'N' : u'6',
    u'O' : u'6',
    u'P' : u'7',
    u'Q' : u'7',
    u'R' : u'7',
    u'S' : u'7',
    u'T' : u'8',
    u'U' : u'8',
    u'V' : u'8',
    u'W' : u'9',
    u'X' : u'9',
    u'Y' : u'9',
    u'Z' : u'9',
    }

def is_alphanum(c):
    return c in ALPHANUM

def char_to_digit(c):
    return DIGIT_MAP.get(c, c)

def process(raw):
    return u''.join(map(char_to_digit, filter(is_alphanum, raw.upper())))

def tel(raw):
    return safe(u'<a href="tel:+1%s">%s</a>' % (process(raw), raw))

register.filter('tel', tel)
