import unittest
from templatetags import tel

class TestEndToEnd(unittest.TestCase):
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
            ]
        for ii, td in enumerate(testdata):
            expected = td['out']
            actual = tel.tel(td['value'])
            msg = 'e: "%s", a: "%s" [%d]' % (expected, actual, ii)
            self.assertEqual(expected, actual, msg)

    def test_safe(self):
        """verify that html is not escaped"""
        from django.template import Template, Context
        t = Template('{% load tel %}{{"4155551212"|tel}}')
        self.assertEqual('<a href="tel:+14155551212">4155551212</a>', t.render(Context()))
