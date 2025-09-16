import sys
input = sys.stdin.readline

n = int(input())
stick = []

for i in range(n):
    a = int(input())
    stick.append(a)

cnt = 1
max = stick[-1]
for i in range(1,n+1):
    if(max < stick[-i]):
        max = stick[-i]
        cnt+=1
print(cnt)

# 앞에서 부터 삥 돌면서 작으면 지우고 큰수가 나오면 그 큰수를 값으로 삼아서 또 삥돌고