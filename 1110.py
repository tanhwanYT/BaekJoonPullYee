import sys
input = sys.stdin.readline

n = int(input())
ans=n
cnt=0

while(1):
    cnt += 1
    num = []
    for i in range(2):
        num.append(n % 10)
        n = n // 10
    n = (num[0]*10) + (sum(num) % 10)
    if(ans == n): break

print(cnt)

#성공!