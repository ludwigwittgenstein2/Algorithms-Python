#!/usr/bin/python

import urllib2

response = urllb2.urlopen('http://python.org/')

html = response.read()

for line in response:
    print line.rstrip()
