
from random import randint
name = input("Enter your name:\n")
result = {True: "Great, you won!!", False: "Oh no, You lose!!"}
res = ['rock', 'paper', 'scissors']
gameplay = {'rock':
"""
          _
    _____/ )
___/  ____/__
     (_|_____)
     (_|_____)
     (_|_____)
_____(_|_____)

 """, 'paper':
"""
   _______
__/  __|__)______________
             ___|____|___)_
              ____|____|___)
             ___|_____|__)
________________|____|__)

""", 'scissors':
"""
   _______
__/  __|__)______________
            { ___|____|___)_
            { _____|____|___)
           (__|___)
____________(_|___)

"""}
win = 0; lose = 0; draw = 0
print("choose one:\n",*gameplay.values(), sep = "\n")
print("Rock, Paper or Scissors?")
for i in range(0,3):
    user = input()
    user = user.lower()
    if user in res:
        computer = res[randint(0,2)]    
        print(f"yourchoice:\n{gameplay[user]}\ncomputer chose:\n{gameplay[computer]}")
        r = result[user.lower() == 'rock' and computer == 'scissors' or user.lower() == 'paper' and computer == 'rock' or user.lower() == 'scissors' and computer == 'paper']
        if user.lower() != computer:
            print(r)
            if r == result[True]:
                win += 1
            else:
                lose += 1
        else:
            print("its a draw")
            draw += 1
    else:
        print("Invalid option")
        exit()
print (f"win - {win}\nlose - {lose}\ndraw - {draw}")
f = open("gamedata", "a")
f.write(f"{name}  wins = {win} | loses = {lose} | draws = {draw}\n")
f.close()