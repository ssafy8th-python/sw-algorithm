t = int(input())

for j in range(t):
    a, b = map(int, input().split())
    if a > b:
        result = '>'
    elif a == b:
        result = '='
    elif a < b:
        result = '<'
    
    print(f'#{j + 1} {result}')