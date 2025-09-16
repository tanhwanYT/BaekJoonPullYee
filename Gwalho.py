import sys
input = sys.stdin.readline

n = int(input())
vp = []
for i in range(n):
    stack = []
    co=True
    st = input().strip()
    vps = list(st)
    start = vps[0]
    if(start == ')'):
        co = False
    else:
        for j in range(len(vps)):
            if(start == vps[j]):
                stack.append(1)
            else:
                if(len(stack) <= 0):
                    co = False
                    break
                else: 
                    del stack[-1]
    if(len(stack) == 0 and co):
        print("YES")
    else:
        print("NO")