django-tel - telephone URL support for Django

This app provides a helper template tag for creating "click to call" URLs, 
as described in RFC 2806: "URLs for Telephone Calls". [0]

The "tel" template tag takes will transform a phone number like string into a
well-formed tel: hyperlink.  This type of link can be clicked to initiate a
phone call in most modern phones capable of viewing web pages.

For example, in your django template:

 {{"415-555-1212"|tel}}

... will render as:

 <a href="tel:+14155551212">415-555-1212</a>

The tel filter also knows how to convert letters:

  {{"800-2-Buy-Now"|tell}}

... will render as:

  <a href="tel:+18002289669">800-2-Buy-Now</a>

django-tel is currently tailored for USA phone networks.  More
international support is planned. Quality patches are appreciated and
accepted.

License: GPL 3

[0] http://www.ietf.org/rfc/rfc2806.txt
