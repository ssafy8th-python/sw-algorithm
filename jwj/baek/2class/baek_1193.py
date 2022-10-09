X = int(input())

line = 1

while X > line:
    X -= line
    line += 1

if line % 2:
    A = line - X + 1
    B = X

else:
    A = X
    B = line - X + 1

print(f'{A}/{B}')

