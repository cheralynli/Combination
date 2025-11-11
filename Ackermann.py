"""
Ackermann Function
This function computes the Ackermann function using recursion.
𝐴(𝑚, 𝑛) = 𝑛 + 1, 𝑖𝑓 𝑚 = 0
𝐴(𝑚, 𝑛) = 𝐴(𝑚 − 1, 1), 𝑖𝑓 𝑚 > 0 𝑎𝑛𝑑 𝑛 = 0
𝐴(𝑚, 𝑛) = 𝐴(𝑚 − 1, 𝐴(𝑚, 𝑛 − 1)), 𝑖𝑓 𝑚 > 0 𝑎𝑛𝑑 𝑛 > 0

"""

def ackerman(m,n):
    if m==0:
       return n+1
    elif m>0 and n==0:
       return ackerman(m-1,1)
    else:
       return ackerman(m-1,ackerman(m,n-1))
    
m= int(input("Enter m: "))
n= int(input("Enter n: "))
print(f"A({m},{n}) = {ackerman(m,n)}")