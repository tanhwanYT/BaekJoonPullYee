import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
num = [n]
leng = n // 5

if(n % 5 == 0):
    print(n // 5)
    exit()

for _ in range(leng):
    n -= 5
    num.append(n)

i=1
while(True):
    if(num[-i] % 2 == 0):
        cnt = len(num) - i
        cnt += num[-i] // 2
        break
    else:
        i += 1

    if(i > len(num)):
        cnt = -1
        break
    
print(cnt)