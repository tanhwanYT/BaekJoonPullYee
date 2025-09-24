import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int,input().split())
graph = []

for i in range(e):
    a,b,edge = map(int, input().split())
    graph.append((edge,a,b))

graph.sort()
result = 0
root = dict()
for i in range(1, v+1): root[i] = i

def find(a):
    if(root[a] == a):
        return a
    else:
        root[a] = find(root[a])
        return root[a]

def union(a, b):
    a = find(a)
    b = find(b)

    root[b] = a

for edge in graph:
    if(find(edge[1]) == find(edge[2])): continue
    else:
        result += edge[0]
        union(edge[1], edge[2])

print(result)