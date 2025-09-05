a = int(input())
b = int(input())
c = int(input())
ans = str(a*b*c)
cnt = len(ans)
v = list(ans)
for i in range(10):
    p=0
    for j in range(cnt):
        if(v[j] == str(i)):
            p += 1
    print(p)