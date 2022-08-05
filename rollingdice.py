
import random
from time import time
import time

player1 = input("Player1's name :") 
player2 = input("Player2's name :")

print(f"Now {player1} one rolls the dice.")
time.sleep(3)

a=random.randint(1, 6)
print(f"{player1}'s score is {a}")

print(f"Now {player2} one rolls the dice.")
time.sleep(3)

b=random.randint(1, 6)

print(f"{player2}'s score is {b}")
time.sleep(3)

if a>b:
    print(f"{player1} is winner.")
    
elif a==b:
    print("Both players tide.")
    
else:
    print(f"{player2} is winner.")