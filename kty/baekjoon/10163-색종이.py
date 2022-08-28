n = int(input())
world = [[0] * 1001 for _ in range(1001)]

for num in range(1, n+1):
    r, c, w, h = map(int, input().split())
    for a in range(w):
        for b in range(h):
            world[r+a][c+b] = num       # 해당 색종이 범위에 num 값을 넣는다. (다음 색종이는 자신의 num값으로 덮어씀)

result = [0] * (n + 1)                  # 해당 num값이 몇개 있는지 확인 하기 위한 카운트배열 생성

for a in range(1001):
    for b in range(1001):
        if world[a][b]:
            result[world[a][b]] += 1

for i in result[1:]:
    print(i)
