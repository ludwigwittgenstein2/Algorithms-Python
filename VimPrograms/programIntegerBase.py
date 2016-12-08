"""Author:Rick Sam
    Date: Oct 8, 2016
    Comments: Vim is a good editor"""

def intString(n,base):
    toConvert = "01234567890ABCDEF"
    if n < base: 
        return toConvert[n]
    else:
        return intString(n//base,base)+toConvert[n%base]

def main():
    print intString(1545,16)

if __name__ == '__main__':
    main()

