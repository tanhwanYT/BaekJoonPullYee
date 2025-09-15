import sys
import math
input = sys.stdin.readline

n = int(input())
paper = []
blue = 0
white = 0
dis = n
x=0
y=0
for i in range(n):
    paper.append(list(map(int,input().split())))

def paperhalf(x,y,dis):
    start = paper[x][y]
    sumidx=0
    same=True
    for i in range(x, x+dis):
        for j in range(y, y+dis):
            if(start != paper[i][j]):
                same = False
                break       
            else:
                sumidx += paper[i][j]
        if(same == False): break

    
    if(sumidx == dis**2 and same):
        return (0,1)
    elif(sumidx == 0 and same):
        return (1,0)
    else:
        w1, b1 = paperhalf(x         , y +dis //2, dis // 2)
        w2, b2 = paperhalf(x + dis//2, y +dis// 2, dis // 2)
        w3, b3 = paperhalf(x + dis//2, y         , dis // 2)
        w4, b4 = paperhalf(x         , y         , dis // 2)
        return (w1+w2+w3+w4, b1+b2+b3+b4)
    
white,blue = paperhalf(x,y,dis)

print(white)
print(blue)