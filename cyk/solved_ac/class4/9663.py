# N-Queen
# NXN 체스판에서 N개의 퀸을 놓는 방법의 수 구하기

def check(row):     # 공격 확인
    for i in range(row):    # 행들 목록
        if visited[row] == visited[i] or abs(visited[row]-visited[i]) == abs(row-i):    # 열의 공격 범위 판별
            return False
    return True

def dfs(k):
    global result

    if k == n:                  # 행의 위치가 n번째 줄이라면 n개의 기물 배치 완료
        result += 1
    else:
        for i in range(n):      # 열
            visited[k] = i      # k행의 i열

            if check(k):        # k행 배치 공격 대상 확인
                dfs(k+1)        # false라면 행의 열 위치 바꿈/ true라면 다음 행으로 넘어가기
n = int(input())

result = 0
visited = [0] * n
dfs(0)
print(result)

