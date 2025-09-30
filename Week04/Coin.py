import sys
input = sys.stdin.readline

t =int(input())

for i in range(t):
    n = int(input())
    coins = list(map(int,input().split()))
    target = int(input())
    dp = [0] * (target + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, target+1):
            dp[j] += dp[j-coin]

    print(dp[target])



# 1을 만드는 경우의수를 dp[1]에 저장 이후 2로갔을때 dp[1]에 있는 값에 coin을 더해서 dp[2]가 됨?