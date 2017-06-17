import os

rootDir = '.'



for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    print('Found directory: %s'% dirName)
    for fname in fileList:
        print('\t%s'%fname)
