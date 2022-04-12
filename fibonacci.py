#fibonacci series

num=int(input("Enter the number of terms : "))
n1=0
n2=1
print(n1)
print(n2)
for i in range(2,num):
    
    next_num=n1+n2
    n1=n2
    n2=next_num
    print(next_num)

