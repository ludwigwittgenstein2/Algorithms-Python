#URLLIB Request

import urllib
import urlparse

x = urllib.urlopen('https://www.duckduckgo.com')

print x.read()

url = 'https://pythonprogramming.net'

values = {'s':'basic', 'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlpen(req)
respData = resp.read()

print respData
