a,b = map(str, input().split())
reserveA = ""
for i in a:
    reserveA = i + reserveA
reserveB = ""
for i in b:
    reserveB = i + reserveB
if(int(reserveA) > int(reserveB)):
    print(reserveA)
else:
    print(reserveB)