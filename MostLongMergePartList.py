import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
dp = [0] * 1001
ans=0
for i in range(n):
    here = 0
    for j in range(i):
        if(num[i] > num[j]):
            here = max(here,dp[j])
    dp[i] = here + 1
    ans = max(ans, dp[i])
print(ans)