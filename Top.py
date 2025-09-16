import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
stack = []
index = [0] * n
for i in range(n):
    while(stack and stack[-1][0] < num[i]): 
        stack.pop()

    if(stack):
        index[i] = stack[-1][1]

    stack.append((num[i], i+1))

print(*index)  
# index.reverse()
# print(index)