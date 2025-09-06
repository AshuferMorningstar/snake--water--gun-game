'''
Snake, Water, Gun Game
1 for Snake
-1 for Water
0 for Gun
'''
import random

computer = random.choice(['1', '-1', '0'])
youstr = input("enter you choice: ")
youdict = {'s': '1', 'w': '-1', 'g': '0'}
reversedict = {'1': 'Snake', '-1': 'Water', '0': 'Gun'}

you = youdict[youstr]
print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if (you == computer):
    print("It's a tie")

else:
    if(computer == -1 and you == 1):
        print("You win")
    elif(computer == 1 and you == -1):
        print("Computer wins")
    elif(computer == 0 and you == 1):
        print("Computer wins")
    elif(computer == 1 and you == 0):
        print("You win")
    elif(computer == -1 and you == 0):
        print("You win")
    elif(computer == 0 and you == -1):
        print("Computer wins")
    else:
        print("Invalid input")
        
            





