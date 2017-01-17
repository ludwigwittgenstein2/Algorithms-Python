#!/bin/Python
"""
Is it Dark outside?
"""

import time

def outside():
        dark = {1:16,2:17,3:18,4:19,5:19,6:20,7:20,8:19,9:18,10:17,11:16,12:16}

        light = {1:8,2:7,3:6,4:5,6:4,7:4,8:5,9:6,10:6,11:7,12:8}

        time_now = time.localtime()

        if time_now.tm_hour >=dark[time_now.tm_mon] or time_now.tm_hour < light[time_now.tm_mon]:
                print "Yes"
        else:
                print "No"

def main():
        outside()

if __name__ == '__main__':
        main()
