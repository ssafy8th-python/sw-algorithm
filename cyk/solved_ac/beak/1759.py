# 암호 만들기
# 서로 다른 L개의 알파벳 소문자들로 구성(최소 한개의 모음 최소 두개의 자음)
# 알파벳이 증가하는 순서로 배열
# 사전식으로 출력


def perm(k,s):
    if k == L:
        cnt1, cnt2 = 0, 0
        for elem in result:
            if elem in ['a', 'e', 'i', 'o', 'u']:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 > 0 and cnt2 > 1:
            print(''.join(result))
        return

    for i in range(s, C):
        if visited[i]:
            result[k] = lst[i]
            visited[i] = False
            perm(k+1, i)
            visited[i] = True


L, C = map(int, input().split())
lst = sorted(list(input().split()))
vow, cons = [], []
result = [-1]*L
visited = [True]*C

perm(0, 0)

