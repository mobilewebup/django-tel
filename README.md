# django-tel - telephone URL support for Django

This app provides template tools for creating "click to call" URLs, as
described in RFC 2806:[URLs for Telephone Calls][0]. The tools are
the `tel` filter, and the `telify` tag.

To use either, first load the tel app with `{% load tel %}` in the
template.

## TEL FILTER

The `tel` template filter transforms a phone number into a well-formed
tel: hyperlink. This type of link can be clicked to initiate a phone
call in phone web browsers.

For example, in your django template:

    {% load tel %}
    {{"415-555-1212"|tel}}

will render as:

    <a href="tel:+14155551212">415-555-1212</a>

Template variables also work seemlessly, of course. If the context
sets phone_number to be "415-555-1212", `{{phone_number|tel}}` will
render as above.

The tel filter also converts letters, like the builtin [phone2numeric
filter][1]:

    {{"800-2-Buy-Now"|tel}}

will render as:

    <a href="tel:+18002289669">800-2-Buy-Now</a>

The tel filter trims numbers with too many digits, useful for
over-long mnemonics:

    {{"800-BUY-IT-NOW"|tel}}

will render as:

    <a href="tel:+18002894866">800-BUY-IT-NOW</a>

## TELIFY TAG

The `telify` tag will locate all phone numbers in a region of text,
and apply the `tel` filter to them.  What is recognized as a phone
number is defined in `tel.PHONE_RE`, a compiled regular expression.

    {% load tel %}
    {% telify %}Call 800-555-1212 to get your free gift today! (Not
    866-555-1212, that is something else entirely.){% endtelify %}

will render as:

    Call <a href="tel:+18005551212">800-555-1212</a> today! (Not <a
    href="tel:+18665551212">866-555-1212</a>, that is something else
    entirely.)

### Be aware: Matching is currently not very intelligent.

If you have HTML like this:

    {# Danger, don't do this! #}
    {% telify %}<img src="/path/to/button.jpg" 
                   alt="Call 800-555-1212"/>
    {% endtelify %}

then that will insert an HTML tag in the alt attribute text.
Highly broken markup, and not what you want. So until `telify` becomes
smarter, please use this tag with care.

`telify` only finds fully numeric numbers. If you want letter-to-number
conversion, you'll have to use the `tel` filter instead. Also, `telify`
only finds ten-digit numbers that include the area code, like
"800-222-3333"; not local numbers like "222-3333".

## INSTALLATION

Simply install the `tel` module. This can be done with the command

    python setup.py install

Or just copy the src/tel directory into the Python path or django apps
directory. Then configure the site as described in USAGE.

## USAGE

1. In settings.py, add the `'tel'` application to `INSTALLED_APPS`.
2. In your templates, you will need to include the module with the
load statement: `{% load tel %}`
3. The `tel` filter and `telify` tag will now be available. Simply write
something like `{{"415-4-PYTHON"|tel}}` in the template.
4. Add `TEL_PREFIX` to your settings.py to change the international prefix.
By default the prefix is `u'+1'`

***Quality patches are appreciated and accepted; see DEV.txt.***

## DEPENDENCIES

Django-tel has only been tested with Python 2.6 and Django 1.2,
running on Linux.  There is no special reason it cannot run (or be
made to run) under less cutting-edge conditions; Python 2.4 and Django
1.0 on Windows, for example. Please contact amax@mobilewebup.com if
you discover any issues.

There are no other dependencies.

## BUGS OR ISSUES?

For any development issues or bug reports related to django-tel,
please also contact Aaron Maxwell at amax@mobilewebup.com .

## FOR DEVELOPERS

Please see DEV.txt.

## LICENSE

GPL 3
Copyright 2009-2010 Aaron Maxwell.

## AUTHOR

Django-tel is sponsored by [Mobile Web Up][2]. If you need expert
assistance in creating websites or web applications that look and feel
great on your customers' hand-held devices, or just need to upgrade
your existing web presence for mobile, we can help.  Visit us at
http://mobilewebup.com/ today.

## CONTRIBUTORS

* International Support - [Level Up][3]
* Read me formatting - [Level Up][3]


[0]: http://www.ietf.org/rfc/rfc2806.txt
[1]: http://docs.djangoproject.com/en/dev/ref/templates/builtins/#phone2numeric
[2]: http://mobilewebup.com/
[3]: http://www.thisislevelup.com

