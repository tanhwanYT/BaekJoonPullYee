import math
def primenum(x):
    for i in range (2, int(math.sqrt(x)) + 1):
    	if x % i == 0:
        	return False
    return True

a = int(input())
cnt =0
num = list(map(int, input().split()))
for i in range(a):
    if(num[i] == 1):
        continue
    elif(primenum(num[i])):
        cnt+=1

print(cnt)

# 복습필요