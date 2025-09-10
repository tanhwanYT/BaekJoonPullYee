import sys
input = sys.stdin.readline

n = int(input())

def Move(n,a,b,v):
    if(n==1):
        print(a, b)
    else:
        Move(n-1,a,v,b)
        print(a, b)
        Move(n-1,v,b,a)

print(2**n-1)

if(n <= 20):
    Move(n,1,3,2)