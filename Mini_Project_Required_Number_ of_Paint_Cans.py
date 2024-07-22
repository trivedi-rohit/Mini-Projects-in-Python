# WAP to estimate the amount of paint required to paint a wall.
import math
def paint(height, width, coverage):
    area = height*width
    n = coverage
    can = math.ceil(area/n)
    print (f"\nThe area of wall is {area} meter sqr. So, You need {round(can)} cans of paint.\n")
h = float(input("Enter the height of wall (in meters) : "))
w = float(input("Enter the width of wall (in meters) : "))
cover = 7 # 1 Can covers 7meter sqr.
paint(height=h,width=w,coverage=cover)