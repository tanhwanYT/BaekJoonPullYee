import sys
input = sys.stdin.readline

n , m = map(int,input().split())
floor = []

for i in range(n):
    tile = str(input())
    floor.append(list(tile))

cnt = 0
for i in range(0, n):
    for j in range(0,m):
        if(floor[i][j] == "-"):
            if(floor[i][j+1] == "-" and j != m-1):
                cnt += 1
        elif(floor[i][j] == "|" and i != n-1):
            if(floor[i+1][j] == "|"):
                cnt += 1
print((n*m) - cnt)

#지능을 조금 낮추고 바라보면 풀수있는 문제