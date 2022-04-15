#list:-it holds heterogenous data , indexed , ordered , duplicate , Multiple values , mutable
#set:-
#tuple
#dictionary

#" CRUD :- CREATE READ/REMOVE UPDATE DELETE "

#crate a list

a=[1,2,3,4,5]
print(a)
b=list(a) #Typecasting #single argument 
print(b)

#append
a.append(26)
print(a)
for i in range(6):
    print(a[i])
# print single
print(a[0])
print(a[5])

#insert :-
a.insert(2,100)
print(a)
