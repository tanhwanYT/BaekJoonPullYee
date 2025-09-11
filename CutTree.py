import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

def treecut(mid, tree,m):
    sum=0
    for i in range(n):
        sum += max(tree[i] - mid, 0)
    return sum >= m

tree = sorted(tree)
highest = max(tree)

lo = 0
hi = highest
result=0

while(lo+1 < hi):
    mid = (lo + hi) // 2
    if(treecut(mid,tree,m)):
        lo = mid
        result = mid
    else:
        hi = mid
print(result)