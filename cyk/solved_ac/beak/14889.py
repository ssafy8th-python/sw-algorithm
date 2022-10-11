# 스타트와 링크
def calc(A, B):
    global res
    a_power, b_power = 0, 0

    for i in range(R):
        for j in range(i+1, R):
            a_power += (arr[A[i]][A[j]] + arr[A[j]][A[i]])
            b_power += (arr[B[i]][B[j]] + arr[B[j]][B[i]])
    if res > abs(a_power - b_power):
        res = abs(a_power - b_power)
    return res

def comb(k, s):
    if k == R:
        team_b = []
        for i in range(N):
            if not i in team_a:
                team_b.append(i)
        calc(team_a, team_b)
        return

    for i in range(s, N-(R-k)+1):
        team_a[k] = i
        comb(k+1, i+1)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
R = N//2
team_a = [-1]*R
res = 10000
comb(0,0)
print(res)