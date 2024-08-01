import os
# All Operations
def addition(a,b):
    result = a+b
    return result
def subtract(a,b):
    result = a-b
    return result
def multipy(a,b):
    result = a*b
    return result
def division(a,b):
    result = a/b
    return result
# Calculator program starts from here.
def calculator():
    num_1 = int(input("Enter a number : "))
    print("Choose operation from given options :\nPress 1 for Addition.\nPress 2 for Subtraction.\nPress 3 for Multiplication.\nPress 4 Division.")
    
    continue_program = True
    while continue_program:
        # print("Choose operation from given options :\nPress 1 for Addition.\nPress 2 for Subtraction.\nPress 3 for Multiplication.\nPress 4 Division.")
        operator = input("Pick an operation: ")
        num_2 = int(input("Enter next number: "))

        if operator == "1":
            output = addition(num_1,num_2)
            print(f"{num_1} + {num_2} = {output}")

        elif operator == "2":
            output = subtract(num_1,num_2)
            print(f"{num_1} - {num_2} = {output}")

        elif operator == "3":
            output = multipy(num_1,num_2)
            print(f"{num_1} * {num_2} = {output}")

        elif operator == "4":
            output = division(num_1,num_2)
            print(f"{num_1} / {num_2} = {output}")
        else:
            print("Choose right option.")
# Check if user want to reuse that value or end the calculation.
        play_again = input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit ").lower()
        if play_again == "y":
            num_1 = output
        
        elif play_again == 'n':
            continue_program = False
            os.system('cls')
            calculator()
        
        else:
            continue_program = False
            print("Bye!")
calculator()



