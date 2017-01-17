from bs4 import BeautifulSoup
import urllib2

import requests

url = "http://www.pythonforbeginners.com"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

print soup.prettify()

print title
