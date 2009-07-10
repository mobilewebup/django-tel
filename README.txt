django-tel - telephone URL support for Django

This app provides a template filter for creating "click to call" URLs,
as described in RFC 2806: "URLs for Telephone Calls". [0]

The "tel" template filter transforms a phone number into a well-formed
tel: hyperlink.  This type of link can be clicked to initiate a phone
call in most modern phones capable of viewing web pages.

For example, in your django template:

 {% load tel %}
 {{"415-555-1212"|tel}}

... will render as:

 <a href="tel:+14155551212">415-555-1212</a>

Template variables also work seemlessly, of course.  If the context
sets phone_number to be "415-555-1212", {{phone_number|tel}} will
render as above.

The tel filter also converts letters, like the builtin phone2numeric
filter [1]:

  {{"800-2-Buy-Now"|tel}}

... will render as:

  <a href="tel:+18002289669">800-2-Buy-Now</a>

The tel filter trims numbers with too many digits...  useful for
over-long mnemonics:
     
  {{"800-BUY-IT-NOW"|tel}}

... will render as:

  <a href="tel:+18002894866">800-BUY-IT-NOW</a>

django-tel is currently tailored for USA phone networks.  More
international support is planned. Quality patches are appreciated and
accepted; see DEV.txt.

INSTALLATION

Simply install the tel module.  This can be done with the command

  python setup.py install

Or just copy the src/tel directory into the Python path or django apps
directory.

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
cannot run (or be made to run) under other conditions; Python 2.4 and
Django 1.0 on Windows, for example.  Please contact amax@hilomath.com
if you discover any issues.

There are no other dependencies.

FOR DEVELOPERS

Please see DEV.txt.

LICENSE
GPL 3

AUTHOR

Django-tel is sponsored by Hilomath Mobile Web Development [2].  If
you need expert assistance in creating websites or web applications
that look and feel great on your customers' hand-held devices, we can
help.  Contact Aaron Maxwell at amax@hilomath.com or visit
http://hilomath.com/ today .

For any development issues or bug reports related to django-tel,
please also contact Aaron Maxwell at amax@hilomath.com .

[0] http://www.ietf.org/rfc/rfc2806.txt

[1] http://docs.djangoproject.com/en/dev/ref/templates/builtins/#phone2numeric

[2] http://hilomath.com/

