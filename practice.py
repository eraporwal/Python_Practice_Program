# 1st internal

print("Q1")
word="I am fine"
n=len(word)
word1=word.upper()
word2=word.lower()
converted_word=""
for i in range(n):
    if i%2==0:
        converted_word+= word2[i]
    else:
        converted_word+= word1[i]
print(converted_word)

print("Q2")
x="Kacha badam"
for i in range(len(x)-1,-1,-1):
    print(i)
    print(x[i])

# print("Q3")
# name=input("What is your name : ")
# age=input("How old are you : ")
# year=str((2022-age)+100)
# print(name+"will be 100 years old in the year"+year)


print("Q4")
n=5
k=5
for i in range (0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=" ")
    print()

print("Q5")
n=int(input("enter number : "))
sum=0
for num in range(1,n+1,1):
    sum=sum+num
print("sum of first",n,"numbers is : ",sum)
average=sum/n
print("Average of ",n,"numbers is : ",average)

# 2nd internal 

print('Q1')
dict1={'first':'sunday','second':'monday'}
dict2={1:3,2:4}
dict1.update(dict2)
print(dict1)

print("Q2")
from math import *
a=2.19
b=3.999999
c=-3.30
print(int(a),floor(b),ceil(c),fabs(c))