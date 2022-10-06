# 치킨 배달
# (r, c) : r행 c열 r과 c는 1부터 시작한다.
# 0은 빈칸 1은 집 2는 치킨집
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
hm = []
store = []

def calc(lst):
    res = 0
    for i in range(H):
        MIN = 10000
        for j in lst:
            tmp = abs(hm[i][0] - store[j][0]) + abs(hm[i][1] - store[j][1])
            if tmp < MIN:
                MIN = tmp
        res += MIN
    return res

def comb(k, s):
    global res
    if k == M:
        temp = calc(result)
        if res > temp:
            res = temp
        return
    for i in range(s, ST-(M-k)+1):
        result[k] = i
        comb(k+1, i+1)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            hm.append([i, j])
        if arr[i][j] == 2:
            store.append([i, j])

result = [-1]*M
ST = len(store)
H = len(hm)
res = 1000000
comb(0,0)
print(res)