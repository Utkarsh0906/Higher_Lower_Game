from data import data
from time import sleep
from random import choice
from os import system
print("Welcome!!")
A = choice(data)
data.remove(A)
cont = True
c = 0
while(True):
    if(len(data)==0):
        print("You won all the rounds!!")
        break
    B = choice(data)
    data.remove(B)
    print("Guess who has more followers on instagram")
    print(f"A: {A['name']}, a {A['description']}, from {A['country']}\nOR")
    print(f"B: {B['name']}, a {B['description']}, from {B['country']}")
    ans = input("Enter your choice A or B: ").upper()
    if(ans == 'A' and A['follower_count'] >= B['follower_count']):
        print("Correct answer!!")
        print(f"{A['name']} has {A['follower_count']}M followers while {B['name']} has only {B['follower_count']}M followers")
        sleep(2)
        system("cls")
        c+=1
    elif(ans == 'B' and A['follower_count'] <= B['follower_count']):
        print("Correct answer!!")
        print(f"{B['name']} has {B['follower_count']}M followers while {A['name']} has only {A['follower_count']}M followers")
        c+=1
        sleep(2)
        system("cls")
        A = B
    else:
        print("Wrong Answer!!")
        print(f"{B['name']} has {B['follower_count']}M followers\n{A['name']} has {A['follower_count']}M followers")
        break
sleep(2)
system("cls")
print(f"Congratulations!! You cleared {c} rounds\nThanks for playing")
    