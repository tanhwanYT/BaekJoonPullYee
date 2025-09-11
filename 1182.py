import sys
from itertools import combinations
input = sys.stdin.readline

n,s = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0

for i in range(1, n+1):
    for j in combinations(num, i):
        if(s == sum(j)): cnt += 1

print(cnt)

# 성공 bitmask?