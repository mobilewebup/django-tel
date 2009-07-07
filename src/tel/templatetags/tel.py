from django import template

register = template.Library()

def tel(value):
    return u'<a href="+1%s">%s</a>' % (value, value)
