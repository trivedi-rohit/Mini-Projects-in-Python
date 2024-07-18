bname = input("Enter boy's first name : ")
gname = input("Enter girl's first name : ")
combine_str = (bname + gname)
comb = combine_str.lower()
t = comb.count('t')
r = comb.count('r')
u = comb.count('u')
e = comb.count('e')
true = t + r + u + e
l = comb.count('l')
o = comb.count('o')
v = comb.count('v')
e = comb.count('e')
love = l + o + v + e
score = str(true)+str(love)
intscore = int(score)
if intscore < 10 or intscore > 90:
    print(f"Your love score is {intscore}% and you go together like 'Coke & Mentos'")
elif intscore >= 40 and intscore <= 50:
    print(f"Your love score is {intscore}% and you are alright together.")
else:
    print(f'Your love score is {intscore}%.')