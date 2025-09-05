x, y, w, h = map(int, input().split())
xc = w - x
yc = h - y
print(min(xc, yc,x,y))