# 거짓말
N, M = map(int, input().split())
tipt = list(map(int, input().split()))
tn, tlst = tipt[0], tipt[1:]
people = [0]*(N+1)
for elem in tlst:
    people[elem] = elem

come_lst = [list(map(int, input().split())) for _ in range(M)]
for _ in range(M):
    for come in come_lst:
        flag = False
        for i in range(1, come[0]+1):
            if people[come[i]]:
                flag = True
                idx = come[i]
                break
        if flag:
            for i in range(1, come[0] + 1):
                if not people[come[i]]:
                    people[come[i]] = idx



cnt = 0
for come in come_lst:
    flag = True
    for elem in come[1:]:
        if people[elem]:
            break
    else:
        cnt += 1
print(cnt)

