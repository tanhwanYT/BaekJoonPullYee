import sys
from itertools import permutations
input = sys.stdin.readline

def count(num):
    return sum(abs(num[i] - num[i+1]) for i in range(n-1))

n = int(input())
num = list(map(int,input().split()))

ans=0
for i in permutations(num, n):
    ans = max(ans, count(i))
print(ans)

# num.sort(reverse=True)
# left = 0
# right = len(num)-1
# newnum = [0] * n

# for i in range(n):
#     if(i%2==0):
#         newnum[i] = num[right]
#         right -= 1
#     else:
#         newnum[i] = num[left]
#         left += 1