class student:
    def avg(self, *x):
        average = 0
        sum = 0
        if len(x)==0:
            average = "NO values Provided"
        else:
            for i in x:
                sum +=i

            average = sum/len(x)
        return average

s1=student()

avg1=s1.avg(12,112,113,215,54,58,78)
avg2=s1.avg(12,13,14)
avg3=s1.avg(12,13)
avg4=s1.avg()

print(avg1)
print(avg2)
print(avg3)
print(avg4)