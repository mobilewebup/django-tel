import re
import string
from django.template.defaultfilters import force_escape
from django.utils.safestring import mark_safe
from django.template import Node
from django.conf import settings


from django import template
register = template.Library()

__all__ = ['tel']

# Max number of digits in phone number, not counting country prefix.  (USA centric)
NUMBER_SIZE = 10

#: alphanumeric
ALPHANUM = string.digits + string.ascii_uppercase

#: Map of alphabet letters to phone digits on a standard touchpad phone
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

#: Telephone number prefix.  (USA centric)
TEL_PREFIX = getattr(settings, "TEL_PREFIX", u'+1')

def is_alphanum(c):
    return c in ALPHANUM

def char_to_digit(c):
    '''
    Replace char with the appropriate numeric digit

    If the character is already a number, just return that.

    '''
    return DIGIT_MAP.get(c, c)

def norm_tel(raw):
    '''
    normalize a telephone number, including converting any letters to numbers

    Strip out any non-numeric characters, after converting any letters to digits.
    Remove leading zeros

    @param raw : The unprocessed number
    @type  raw : unicode

    @return    : A normalized telephone number
    @rtype     : unicode
    
    '''
    return u''.join(map(char_to_digit, filter(is_alphanum, raw.lstrip("0").upper())))[:NUMBER_SIZE]

def tel(raw):
    '''
    Create click-to-call URL anchor tag from a telephone number

    This is the Django template filter.  The returned string is an
    HTML snippet: an anchor tag for a telephone number.  For example,
    call tel('(415)555-1212') will yield the HTML
    '<a href="+14155551212">(415)555-1212</a>'.

    The returned string is marked safe, so that the HTML will not be
    escaped when rendered.
    
    EXCEPTION: As a protection, if the filter input is so unlike an
    actual phone number that it contains any HTML-unsafe characters
    (such as a greater-than sign), tel will return the string
    untransformed, in a way that the template engine will then escape.
    This is to ensure the final response will contain no broken HTML,
    no matter what is filtered.

    '''
    for c in u'<>\'"&':
        if c in raw:
            return force_escape(raw)
    return mark_safe(telurl(raw))

def telurl(phone):
    """
    create a tel anchor tag for a phone number
    
    @param phone : Phone number
    @type  phone : unicode

    @return      : tel anchor tag
    @rtype       : unicode
    
    """
    return u'<a href="tel:%s%s">%s</a>' % (TEL_PREFIX, norm_tel(phone), phone)

register.filter(u'tel', tel)

#: regular expression that's meant to find phone numbers in blocks of text
PHONE_RE = re.compile(r'(\d{3}[.-]?\d{3}[.-]?\d{4}|\(\d{3}\)[.-]?\d{3}[.-]?\d{4})')

def telify_text(text):
    """
    Find all phone numbers in text, and replace them with click-to-call URLs

    @param text : Text containing 0 or more phone numbers
    @type  text : unicode

    @return     : Same text, with phone numbers replaced with tel HTML anchor tags
    @rtype      : unicode
    
    """
    def telurl_match(phone_match):
        return telurl(phone_match.group(1))
    return PHONE_RE.sub(telurl_match, text)

class TelifyNode(Node):
    """
    Node for applying telify transformation
    """
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        return telify_text(self.nodelist.render(context))

def do_telify(parser, token):
    """
    Apply the telify tag transformation to a section of text
    """
    nodelist = parser.parse(('endtelify',))
    parser.delete_first_token()
    return TelifyNode(nodelist)

register.tag(u'telify', do_telify)
