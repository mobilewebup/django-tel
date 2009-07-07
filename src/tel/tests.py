import unittest
from templatetags import tel

class TestEndToEnd(unittest.TestCase):
    def test_main(self):
        testdata = [
            {'value' : u'4155551212',
             'out'   : u'<a href="+14155551212">4155551212</a>',
             },
            {'value' : u'415-555-1212',
             'out'   : u'<a href="+14155551212">415-555-1212</a>',
             },
            {'value' : u'(415)555-1212',
             'out'   : u'<a href="+14155551212">(415)555-1212</a>',
             },
            ]
        for ii, td in enumerate(testdata):
            expected = td['out']
            actual = tel.tel(td['value'])
            msg = 'e: "%s", a: "%s" [%d]' % (expected, actual, ii)
            self.assertEqual(expected, actual, msg)
