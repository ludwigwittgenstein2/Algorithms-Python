#!/usr/bin/Python

def KMPSearch(txt, pat):

#   txt = raw_input("Entr the String or Paragraph:")
#   pat = raw_input("Enter pattern to Search:")
#   len[txt] = 6
#   len[pat] = 2
    lps = len(pat)

    i = 0
    j = 0
    while i < len(txt):
        if txt[i] == pat[j]:
            i += 1
            j += 1
            print txt[i], pat[j]
        if j == lps:
            print "found"
def main():
    txt = "AAABBC"
    pat = "AA"
    KMPSearch(txt, pat)

if __name__ == '__main__':
    main()
