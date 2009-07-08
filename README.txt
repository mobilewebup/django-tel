django-tel - telephone URL support for Django

This app provides a helper template filter for creating "click to
call" URLs, as described in RFC 2806: "URLs for Telephone Calls". [0]

The "tel" template filter takes will transform a phone number like
string into a well-formed tel: hyperlink.  This type of link can be
clicked to initiate a phone call in most modern phones capable of
viewing web pages.

For example, in your django template:

 {% load tel %}
 {{"415-555-1212"|tel}}

... will render as:

 <a href="tel:+14155551212">415-555-1212</a>

The tel filter also knows how to convert letters:

  {{"800-2-Buy-Now"|tel}}

... will render as:

  <a href="tel:+18002289669">800-2-Buy-Now</a>

The tel filter knows how to trim numbers with too many digits...
useful for over-long mnemonics:
     
  {{"800-BUY-IT-NOW"|tel}}

... will render as:

  <a href="tel:+18002894866">800-BUY-IT-NOW</a>

django-tel is currently tailored for USA phone networks.  More
international support is planned. Quality patches are appreciated and
accepted; see DEV.txt.

INSTALLATION

Simply install the tel module.  This can be done with the command

  python setup.py install

Or just copy the src/tel directory into the Python path.

USAGE

1) In settings.py, add the 'tel' application to INSTALLED_APPS.

2) In your templates, you will need to include the module with the
load statement:

 {% load tel %}

3) The tel filter will now be available.  Simply write something like
{{"415-4-PYTHON"|tel}} in the template.

DEPENDENCIES

So far, django-tel has only been tested with Python 2.6 and the beta
release of Django 1.1, running Linux.  There is no special reason it
cannot be made to run under other conditions (Python 2.4 and Django
1.0 on Windows, for example).  Please contact amax@hilomath.com if you
discover any issues.

There are no other dependencies.

KNOWN ISSUES

django-tel works well for USA-like phone number formats.  Right now,
it unfortunately ignores the rest of the world.  (How impolite!)  The
plan is to remedy this eventually.

FOR DEVELOPERS

Please see DEV.txt.

LICENSE
GPL 3

AUTHOR

Django-tel is sponsored by Hilomath Mobile Web Development [1].  If
you need expert assistance in creating websites or web applications
that look and feel great on your customers' hand-held devices, we can
help.  Contact Aaron Maxwell at amax@hilomath.com or visit
http://hilomath.com/ today .

For any development issues or bug reports related to django-tel,
please also contact Aaron Maxwell at amax@hilomath.com .

[0] http://www.ietf.org/rfc/rfc2806.txt

[1] http://hilomath.com/
