#arbitarary arguments
def avg (* value):
    x=0
    for i in (value):
        x=x+i
    print(len(value))
    print(x)
    return x/len(value)
y=avg(1,2,3)
print(y)