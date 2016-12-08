"""Author:Rick Sam
   Oct 30,2016
   Comments: Recursion to sum the numbers
   Find out the same of first 10 numbers by using recursion
   """


def use_Recursion(n):
        if n == 1:
                return
        sum(use_Recursion(n) + use_Recursion(n-1))

def main():
        n = 10
        use_Recursion(n)
        print n
if __name__=='__main__':
        main()

