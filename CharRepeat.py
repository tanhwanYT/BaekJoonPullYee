a = int(input())
for i in range(a):
    cnt, n = input().split()
    cnt1 = int(cnt)
    m = list(n)
    for j in m:
        for l in range(cnt1):
            print(j, end="")
    print()