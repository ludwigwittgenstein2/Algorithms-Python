#!/usr/bin/Python

def KMPSearch(txt, pat):

#   txt = raw_input("Entr the String or Paragraph:")
#   pat = raw_input("Enter pattern to Search:")
    lps = len(pat)

    i = 0
    while i <len(txt):
        for j in range(lps):
            print txt[i], pat[j]
        i += 1


def main():
    txt = raw_input("Entr the String or Paragraph:")
    pat = raw_input("Enter pattern to Search:")
    KMPSearch(txt, pat)

if __name__ == '__main__':
    main()
