import sys
input = sys.stdin.readline

n = int(input())
apart = []
cnt = [0] * n

for i in range(n):
    num = int(input())
    apart.append(list(num))

def dfs(apart, node):
    if(node != 0):
        cnt[node] += 1
    

for i in range(n):
    for j in range(n):
        dfs(apart, apart[i][j])
#못품 배열을 돌면서 돈 인덱스는 0으로 표시 이후 카운트