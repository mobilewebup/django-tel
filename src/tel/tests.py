import unittest
from django.template import Template, Context
from templatetags import tel

class Test_tel_filter(unittest.TestCase):
    def test_main(self):
        testdata = [
            {'value' : u'4155551212',
             'out'   : u'<a href="tel:+14155551212">4155551212</a>',
             },
            {'value' : u'415-555-1212',
             'out'   : u'<a href="tel:+14155551212">415-555-1212</a>',
             },
            {'value' : u'(415)555-1212',
             'out'   : u'<a href="tel:+14155551212">(415)555-1212</a>',
             },
            # convert letters
            {'value' : u'415-555-ROCK',
             'out'   : u'<a href="tel:+14155557625">415-555-ROCK</a>',
             },
            {'value' : u'415-555-rock',
             'out'   : u'<a href="tel:+14155557625">415-555-rock</a>',
             },
            {'value' : u'415-555-roCK',
             'out'   : u'<a href="tel:+14155557625">415-555-roCK</a>',
             },
            {'value' : u'415-JKL-ROCK',
             'out'   : u'<a href="tel:+14155557625">415-JKL-ROCK</a>',
             },
            {'value' : u'415-JJJ-WXYZ',
             'out'   : u'<a href="tel:+14155559999">415-JJJ-WXYZ</a>',
             },
            {'value' : u'800-2-Buy-Now',
             'out'   : u'<a href="tel:+18002289669">800-2-Buy-Now</a>',
             },
            # chop off excess digits
            {'value' : u'800-BUY-IT-NOW',
             'out'   : u'<a href="tel:+18002894866">800-BUY-IT-NOW</a>',
             },
            ]
        for ii, td in enumerate(testdata):
            expected = td['out']
            actual = tel.tel(td['value'])
            msg = 'e: "%s", a: "%s" [%d]' % (expected, actual, ii)
            self.assertEqual(expected, actual, msg)

    def test_safe(self):
        """verify that html is not escaped"""
        t = Template('{% load tel %}{{"4155551212"|tel}}')
        self.assertEqual('<a href="tel:+14155551212">4155551212</a>', t.render(Context()))

    def test_varsub(self):
        """Verify variable substitution works"""
        t = Template('{% load tel %}{{somevar|tel}}')
        self.assertEqual('<a href="tel:+14155551212">4155551212</a>', t.render(Context({'somevar' : '4155551212'})))

class Test_telify_tag(unittest.TestCase):
    def test_telify_text(self):
        testdata = [
            # degenerate cases
            {'in'  : '',
             'out' : '',
             },
            {'in'  : 'something',
             'out' : 'something',
             },
            {'in'  : '<p><strong>Not</strong> a phone number.</p>',
             'out' : '<p><strong>Not</strong> a phone number.</p>',
             },
            ]
        for ii, td in enumerate(testdata):
            expected = td['out']
            actual = tel.telify_text(td['in'])
            msg = 'e: "%s", a: "%s" [%d]' % (expected, actual, ii)
            self.assertEqual(expected, actual, msg)
