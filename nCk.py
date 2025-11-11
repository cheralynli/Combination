"""
This program calculates nCk of a number using recursive methods
 """

def c(n,k):
    if k == 0:
        return 1
    elif k>n:
        return 0
    else:
        return c(n-1,k-1) + c(n-1,k)
    
n= int(input("Enter n: "))
k= int(input("Enter k: "))
print(f"{n}C{k} = {c(n,k)}")