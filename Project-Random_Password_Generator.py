# Random Password Generator:
#! Methos -1 :
import random
import string
# lower = list(string.ascii_lowercase) 
# upper = list(string.ascii_uppercase) 
# letters = upper + lower
letters = list(string.ascii_letters)
number = list(string.digits)
symbols = list(string.punctuation)
print("Welcome to Password Generator!")
let = int(input("How many letters would you like in your password? "))
sym = int(input("How many symbols would you like? "))
num = int(input("How many numbers would you like? "))
pswd_length = (let+ sym + num)
print(f"Your password length is {pswd_length}.")
password = ""
for i in range(1,let+1):
    char = random.choice(letters)
    password += char
for i in range(1,sym+1):
    psym =  random.choice(symbols)
    password += psym
for i in range(1,num+1):
    pdig = random.choice(number)
    password += pdig
# print(password) #! Fixed pattern password    
random_password = ''.join(random.sample(password, len(password))) #! Randomised password
print(f"Your password is {random_password}")

#! Method - 2 :
import random 
import string
password = ''
print('\nWelcome to password generator')
words=[random.choice(string.ascii_letters) for i in range(int(input("Enter how many letters : ")))]
numbers=[random.choice(string.digits) for i in range(int(input("Enter how many numbers : ")))]
symbol=[random.choice(string.punctuation) for i in range(int(input("Enter how many symbols : ")))]
sum_pswd = words + numbers + symbol
random.shuffle(sum_pswd)
for i in sum_pswd:
    password += i
print(password)

