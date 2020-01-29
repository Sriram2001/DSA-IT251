def itFib(n):
    num=[]
    first=0
    second=1
    num.append(0)
    num.append(1)
    for i in range(3,n+1):
        third = first+second
        num.append(third)
        first=second
        second=third
    return num

def rcFib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return rcFib(n-1)+rcFib(n-2)

n = int(input("Enter number: "))

itarr = itFib(n)
print(itarr)

arr=[]
for i in range(1,n+1):
    arr.append(rcFib(i))
print(arr)