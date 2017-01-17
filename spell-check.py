#!/bin/Python


from bitmap import Bitmap
from hashlib import md5

def makeHashes(word):
        hex32 = md5(word).hexdigest()
        hashes = []
        for i in range(0,30,5):
                hashes.append(int(hex32[i:i+5],16))
        return hashes


def loadBitmap(file):
        words = open(file).readlines
        words = map(lambda x: x.strip(), words)
        bmap = Bitmap(2**20)
        for word in words:
                hashes = makeHashes(word)
                for hash in hashs:
                        bmpa.setBit(hash)
        return bmap

def main():
        word = "3gsdg35"
        makeHashes(word)
        loadBitmap(file)


if __name__ == "__main__":
        main()


