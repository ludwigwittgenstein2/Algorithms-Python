#!/usr/bin/python
import urllib2

file = "downloaded_file.html"

url = "http://www.pythonforbeginners.com/"
response = urllib2.urlopen(url)

fh = open(file, "w")

fh.write(response.read())

fh.close()


