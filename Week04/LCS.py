import sys
input = sys.stdin.readline

x =list(str(input().strip()))
y =list(str(input().strip()))
x, y = [" "] + x, [" "] + y
n,m = len(x)-1, len(y)-1

dp = [[0]*(m+1) for _ in range(n+1)]

def LCS(x, y):
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            if(x[i] == y[j]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    # n,m = len(x), len(y)
    # if(n==0 or m==0): return
    # if(x[-1] == y[-1]):
    #     return LCS(x[-2], y[-2]) + 1
    # else:
    #     return max(LCS(x, y[-1]), LCS(x[-1], y))
    
LCS(x,y)
print(dp[n][m])