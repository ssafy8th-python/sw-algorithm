# 토너먼트 카드게임
# 분할정복 알고리즘 / 병합정렬
def game(start, end):
    if start == end:    # 한개일때
        return start
    left = game(start, (end + start) // 2)
    right = game(((end + start) // 2)+1, end)
    if (s[left] == 3 and s[right] == 1) or (s[left] == 1 and s[right] == 2) or (s[left] == 2 and s[right] == 3):
        return right
    else:
        return left



# 1: 가위, 2: 바위, 3: 보
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    s = list(map(int, input().split()))
    print(f'#{tc} {game(0, n-1)+1}')