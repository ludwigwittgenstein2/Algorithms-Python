"""Author:Rick Sam
   Date: Oct 21, 2016
   Comments: I wonder how this is a Theta(n) running time problem?"""

def is_prime(n):
        for i in range(2,n):
                if n % i == 0:
                        return False
                return True

def main():
        n = int(input("Enter the number to check if it is prime or not:"))
        print is_prime(n)

if __name__ == '__main__':
        main()

