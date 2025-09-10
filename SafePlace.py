import sys
input = sys.stdin.readline

n = int(input())
safe = [][]
rain = [][]

for i in range(n):
    for j in range(n):
        rain[i][j] = int(input())
        if(rain[i][j] > 4): safe[i][j] = 1
        else: safe[i][j] = 0

dx=[0,0,-1,1] 
dy=[-1,1,0,0]

for i in range(len(safe)):
    for j in range(len(safe[i])):
        for k in range(4):
            testX = i + dx[i]
            testY = j + dy[i]