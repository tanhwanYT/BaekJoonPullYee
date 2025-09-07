maxX, maxY = map(int, input().split())
n = int(input())

cutX = [0, maxX] 
cutY = [0, maxY]  

for _ in range(n):
    s, num = map(int, input().split())
    if s == 0:  
        cutY.append(num)
    else:        
        cutX.append(num)

cutX.sort()
cutY.sort()

diffs = []
for i in range(len(cutX)-1):
    diffs.append(cutX[i+1] - cutX[i])
maxWidth = max(diffs)

diffs = []
for i in range(len(cutY)-1):
    diffs.append(cutY[i+1] - cutY[i])
maxHeight = max(diffs)

print(maxWidth * maxHeight)