import sys
input = sys.stdin.readline

N, M = map(int, input().split())

t_person = list(map(int, input().split()))
t_person = set(t_person[1:])

party = [[] for _ in range(M)]
can_visit = [True] * M

result = M

for p in range(M):
    arr = list(map(int, input().split()))
    for num in arr[1:]:
        party[p].append(num)

# 파티의 수 만큼 반복
for _ in range(M):
    for i in range(M):
        if can_visit[i]:
            for p in t_person:
                if p in party[i]:
                    result -= 1
                    can_visit[i] = False
                    for k in party[i]:
                        t_person.add(k)
                    break

print(result)
