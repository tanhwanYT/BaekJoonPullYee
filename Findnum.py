import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
m = int(input())
find = list(map(int,input().split()))

num = sorted(num)

def binarySearch(i,n,num):
    s=0
    e=n
    mid = (s+ e) // 2
    while(s!=e):
        if(num[mid] == i):
            return True
        elif(num[mid] > i): e = mid
        elif(num[mid] < i): s = mid+1
        mid = (s+e)//2   
    return False

for i in find:
    if(binarySearch(i,n,num)):
        print("1")
    else:
        print("0")
    