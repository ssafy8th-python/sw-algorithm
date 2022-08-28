w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# w, h는 독립되어 있기 때문에 따로 봐도 된다.
# 개미는 1초에 1만큼 가므로 t초 후에는 현재 위치 p에서 t만큼 진행 p + t
# 갔다가 다시 돌아오므로 한 사이클은 2 * w
# 따라서 개미의 현재 위치는 간 거리 (p + t) % (2 * w)
# 이떄 나머지 값이 원래 w의 길이보다 크다면 개미가 w까기 갔다가 돌아오고 있는 중이므로
# 총 길이 2 * w에서 나머지 값을 빼주면 현재 개미의 위치를 구할 수있다.
# h 값도 동일
x = (p + t) % (2 * w)
y = (q + t) % (2 * h)

x = 2 * w - x if x > w else x
y = 2 * h - y if y > h else y

print(x, y)


