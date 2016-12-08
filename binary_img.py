#!/bin/Python

#Get a binary number from user
#img_in = input("Enter a bitmap image")
with open('/Users/Rick/Algorithms_PythonBook/rick2014.jpg') as w:
        img_in = w.read()

#Initially there is no output
img_out = ""

for row in img_in:
        if row == "1":
                img_out = img_out + "*"
        else:
                img_out = img_out + ""
        print img_out

