""" Author: Rick Sam
    Purpose: Finding what Exception Finally does
    Book: ByteCode
    Comments: I think, it's a good book to re-read the basics
    Last lesson Learnt: I learn that I can open Python library files and
    learn from them, Why didn't I think of this before?
    Gosh, horrible of me.
    """
import sys
import time
import cProfile

def practiceFinally():
    f = None
try:
    f = open("poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
        sys.stdout.flush()
        print "Press ctrl+c now"
        time.sleep(2)
except IOError:
    print "Could not find poem.txt"
except KeyboardInterrupt:
    print "!! You cancelled the reading from the file."
finally:
    if f:
        f.close()
    print "(Cleaning up:Closed the file)"


print cProfile.run('practiceFinally')
