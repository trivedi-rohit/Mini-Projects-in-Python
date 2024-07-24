# Find if number is prime number or not.
#! Method -1 
import math
def prime (n):
    if n>1:
        my_prime = True
        # for i in range(2, n):
        for i in range(2, math.ceil(n/2)+1):
            if n % i == 0: 
                my_prime = False
        if my_prime == True:
            print("Given number is a Prime Number")   
        else:
            print("Not a prime number") 
    else:
        print("Not a prime number")    
num = int(input("Enter a number : "))
prime(num)

#! Method -2
import math 
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
n = int(input("Enter a number : "))
print(prime(n))
