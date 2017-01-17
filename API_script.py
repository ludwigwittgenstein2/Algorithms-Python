#!/usr/bin/Python

import json
import sys
import urllib2
import os


usage = """
Usage:./tweet_search.py'keyword'
e.g./tweet_search.py pythonforbeginners
Use "+" to replace whitespace"
e.g ./tweet_search.py"python+for+beginners"
"""

if len(sys.argv)!=2:
        print usage
        sys.exit(0)

screen = sys.argv[1]

url = urllib2.urlopen("http://search.twitter.com/search.json?q="+screen)

data = json.load(url)

print len(data), "tweets"

for tweet in data['results']:
        print tweet['text']

for status in data['results']:
        print "%s %s" %(status["created_at"], status["text"])

