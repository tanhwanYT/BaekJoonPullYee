import sys
input = sys.stdin.readline

n , k = map(int,input().split())
virus = []

for i in range(n):
    num = list(map(int,input().split()))
    virus.append(num)

s, x, y = map(int,input().split())

maxXY = n-1

print(virus[x-1][y-1])

#못품