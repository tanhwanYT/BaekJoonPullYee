max = 0
maxn = 1
for i in range(1,10):
    a=int(input())
    if(max < a):
        max = a
        maxn = i
print(max)
print(maxn)