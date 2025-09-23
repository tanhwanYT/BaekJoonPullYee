import sys
input = sys.stdin.readline

v, e = map(int,input().split())
graph = [][]

for i in range(v): graph[i][i] = 0
for i in range(e):
    n, m, index = map(int,input().split())
    graph[n][m] = index
    graph[m][n] = index

def spaning(n, sum):
    next = 0
    for i in range(v):
        if(graph[n][i] != None):
            sum += graph[n][i]
            next = i

    spaning(next, sum)

sum = 0
spaning(1, sum)

#그래프 스패닝 하는법? 처음거 들어간 다음 연결하는 엣지있는지 검사 그거 반복 만들기 개 힘드네 이거 