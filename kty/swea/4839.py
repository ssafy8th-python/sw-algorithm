import sys

sys.stdin = open("input_4839.txt", "r")

T = int(input())
for tc in range(1, T+1):
    P, A, B = list(map(int, input().split()))

    P = list(range(1, P+1))
    N = len(P)

    def search(key):
        st = 0
        ed = N - 1
        cnt = 0
        while st <= ed:
            c = (st + ed) // 2
            cnt += 1
            if P[c] == key:
                break
            elif P[c] < key:
                st = c
            else:
                ed = c
        return cnt

    cnta = search(A)
    cntb = search(B)

    def vs(cnta, cntb):
        if cnta > cntb:
            return 'B'
        elif cnta < cntb:
            return 'A'
        else:
            return 0

    print(f'#{tc} {vs(cnta, cntb)}')