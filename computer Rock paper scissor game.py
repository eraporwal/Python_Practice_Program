# Rock paper scissor game
from random import randint

print("Enter 1 for rock\nEnter 2 for paper\nEnter 3 for scissor")

p1=int(input("Player\nEnter Your Choice : "))
import random

p2=(random.randint(1,3))
print("Computer Choice is ",p2)
if(p1<1 or p1>3):
    print("Player 1 please enter a valid Number!!!")
elif(p1==p2):
    print("Match Draw!!!!!!!!!")
elif(p1==1 and p2==2):
    print("Player Computer(Paper) has Won!!!!!!!!!")
elif(p1==1 and p2==3):
    print("Player 1(Rock) has Won!!!!!!!!!")
elif(p1==2 and p2==1):
    print("Player 1(Paper) has Won!!!!!!!!!")
elif(p1==2 and p2==3):
    print("Player Computer(Scissor) has Won!!!!!!!!!")
elif(p1==3 and p2==1):
    print("Player Computer(Rock) has Won!!!!!!!!!")
elif(p1==3 and p2==2):
    print("Player 1(Scissor) has Won!!!!!!!!!")
