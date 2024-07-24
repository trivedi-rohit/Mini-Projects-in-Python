#! Method -1
def factorial(num):
    if num < 0:
        print(f"Factorial of {num} can't be determined.")
    elif (num ==1 or num == 0):
        return 1
    else:
        # return num*factorial(num-1)
        facto = 1
        while(num > 1):
            facto *= num
            num -= 1
        return facto
number = int(input("Enter a number : "))
# print("Factorial of", number, "is", factorial(number))
print(f"Factorial of {number} is {factorial(number)}")

#! Method - 2
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
num = 9
print(f"Factorial of {num} is {factorial(num)}")