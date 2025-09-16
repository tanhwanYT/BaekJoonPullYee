import sys
input = sys.stdin.readline

n = int(input())
num = []

for i in range(n):
    k = int(input())
    if(k == 0):
        del num[-1]
    else:
        num.append(k)

print(sum(num))