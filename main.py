import random

comp = random.choice([0,-1,1])
your_str = input("enter your choice : ")
your_dict = {'s' : 1,'w' : -1 , 'g' : 0}
rev_dict = {1 : 's', -1 : 'w', 0 : 'g'}

you = your_dict[your_str]
print(f"your choice is {rev_dict[you]}, comp choice is {rev_dict[comp]}")

if comp == you:
    print("match tie")
else:
    if (comp == 1 and you == -1) or (comp == -1 and you == 0) or (comp == 0 and you == 1):
        print("you lose")
    else:
        print("you win") 