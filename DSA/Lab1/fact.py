def recFact(n):
    if n == 0 :
        return 1
    else :
        return n* recFact(n-1)

def itFact(n):
    if n == 0:
        return 1
    k=1
    for i in range(n,0,-1):
        k *= i
    return k

n = int(input("Enter number: "))
print('Factorial is:')
print("Recursive:",recFact(n))
print('Iterative:',itFact(n))