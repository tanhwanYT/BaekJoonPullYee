import sys
from itertools import combinations
input = sys.stdin.readline

n = [int(input()) for _ in range(9)]
ans = []
for i in combinations(n,7):
    if(sum(i) == 100):
        sys.stdout.write("\n".join(map(str, sorted(i))))
        break