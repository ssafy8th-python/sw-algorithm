# 달팽이는 올라가고 싶다
# 낮 : A 만큼 상승 밤 : B만큼 하강 -> 정상에 올라간 후 미끄러지지 않음
# 나무 막대를 모두 오르려면 며칠이 걸리는가


A, B, V = map(int, input().split())

if (V-A) % (A-B) == 0:
    print((V-A) // (A-B) + 1)
elif (V-A) % (A-B) != 0:
    print((V-A) // (A-B) + 2)
