# 카드 2
# 제일 위에 있는 카드를 바닥에 버린다 그 다음 제일 위에 있는 카드를 맨 킽으로 옮긴다 한장 남을 때까지 반복 후 남은 카드 구하기
# 시간복잡도 list => O(n) deque => O(1)
import collections

n = int(input())

a = collections.deque(range(2, n+1, 2)) # 짝수만 => 홀수 카드는 첫시행에서 전부 사라짐
if n ==1: # 카드 개수가 한 장일때는 1출력
    print(1)

if n % 2: # 홀수
    while len(a) > 1: # 길이에 따라 다르게 시행
        b = a.popleft()
        a.append(b)
        a.popleft()
else:
    while len(a) > 1:
        a.popleft()
        b = a.popleft()
        a.append(b)

print(*a)


