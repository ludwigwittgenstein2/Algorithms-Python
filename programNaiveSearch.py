# Python program for Naive Pattern Searching
# Compare this code with my Code.
def search(pat, txt):
    M = len(pat)
    N = len(txt)
    # M = 10, N = 4
    # A loop to slide pat[] one by one
    for i in xrange(N-M+1):
        print "this is printing"+ str(i)
        # For current index i, check for pattern match
        for j in xrange(M):
            print "this is i+j:"+ str(i+j)
            if txt[i+j] != pat[j]:
                break
        if j == M-1: # if pat[0...M-1] = txt[i, i+1, ...i+M-1]
            print "Pattern found at index " + str(i)

# Driver program to test the above function
txt = "AABAACAADAABAAABAA"
pat = "AABA"
search (pat, txt)


def naiveSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    for i in xrange(N-M+1):
        print "This is printing" + str(i)
        for j in xrange(M):
            print "this is i+j:" + str(i+j)
            if txt[i+j] != pat[j]:
                break
        if j == M -1:
            print "This pattern is found at index" + str(i)

if __name__ == '__main__':
#   txt = "Luderman Gottlieb"
#   pat = "Luderman"
#   naiveSearch(pat, txt)
    search()
