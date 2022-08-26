garo, sero = map(int, input().split())
line = int(input())
row = [0, sero]
col = [0, garo]
for _ in range(line):
    d, num = map(int, input().split())
    if d == 0:
        row.append(num)
    else:
        col.append(num)

row.sort()
col.sort()
maxR = 0
maxC = 0

for i in range(1, len(row)):
    if row[i]-row[i-1] > maxR:
        maxR = row[i]-row[i-1]

for i in range(1, len(col)):
    if col[i]-col[i-1] > maxC:
        maxC = col[i]-col[i-1]

print((maxR) * (maxC))