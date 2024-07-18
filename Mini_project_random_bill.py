#Random bill payment b/w friends.
import random
#! Method -1
# frnds= input("Enter the names of your friends : ").split()
# print("Friends : ", frnds)
# rslt = random.choice(frnds)
# print(f"{rslt}, will pay the bill.") 

#! Method -2
# names = (input("Enter names of friends : "))
# splitted =names.split()
# print("Friends : ", splitted)
# length = len(splitted)
# bs = random.randint(0,length-1)
# print(splitted[bs], "will pay the bill.")

#! Method -3
names = str(input("Enter names of friends (using comma) : ")).split(",")
print("Friends : ", names)
length = len(names)
bs = random.randrange(0,length)
print(f"{names[bs]} will pay the bill.")