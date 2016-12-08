"""Author:Rick Sam
    Date: Oct 8, 2016
    Comments: Just started using Vim"""

def isPalindrome():
    '''Checks if it is palindrome or not'''
    if string1 == string2:
      return "This is Palindrome" 
    return "This is not Palindrome"

def isPalindromeEasy(string):
    '''Easiest way to Check.'''
    if string == string[::-1]:
        return "It is a Palindrome"
    return "It is not a Palindrome"

       
def main():
#    string1 = input('Enter the name:')
#    string2 = string[::-1]
#    isPalindrome(string1,string2)
    string = "Rick"
    isPalindromeEasy(string)

if __name__=='__main__':
    main()

