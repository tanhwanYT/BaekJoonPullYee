n = int(input())
line = [0] * n
for i in range(n):
    line[i] = int(input())

line = sorted(line)

for i in range(n):
    print(line[i])