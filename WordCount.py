a = list(map(str, input().split(" ")))
cnt=0
for i in a:
    if(i.isalpha()):
        cnt += 1
print(cnt)