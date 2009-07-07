from django import template
import string

register = template.Library()

def process(raw):
    return filter(lambda c: c in string.digits, raw)

def tel(raw):
    return u'<a href="+1%s">%s</a>' % (process(raw), raw)
