django-tel - telephone URL support

This app provides a helper template tag for creating "click to call" URLs, 
as described in RFC 2806: "URLs for Telephone Calls". [0]

The "tel" template tag takes will transform a phone number like string into a
well-formed tel: hyperlink.  This type of link can be clicked to initiate a
phone call in most modern phones capable of viewing web pages.

For example, in your django template:

{{"415-555-1212"|tel}}

... will render as:

<a href="tel:+14155551212">415-555-1212</a>

[0] http://www.ietf.org/rfc/rfc2806.txt
