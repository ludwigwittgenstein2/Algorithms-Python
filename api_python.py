#!/usr/bin/Python

"""
API Tutorial
"""

import urllib2
import json

url = 'http://api.duckduckgo.com/?q=valley+forge+national+park&format=json&pretty=1'
json_obj = urllib2.urlopen(url)

data = json.load(json_obj)

print data
