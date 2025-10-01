import sys
input = sys.stdin.readline

n, k =map(int, input().split())
coin = []

for i in range(n): coin.append(int(input()))
coin.sort(reverse=True)
cnt = 0

for i in coin:
    if(i <= k):
        while(k >= i):
            cnt += 1
            k -= i

print(cnt)