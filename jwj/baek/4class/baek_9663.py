N = int(input())


def is_ok(row):

    # 세로 확인 : 열의 값을 확인합니다.
    # 대각선 확인 : 두개의 행의 값을 뺀 것과 두개의 열의 값을 뺀 것이 같으면 같은 대각선에 있다고 판단
    # 대각선 방향으로 행과 열의 같이 일정하게 변하기 때문에 가능
    # ex) 3,3 | 2,2   => 3-2 = 1, 3-2 = 1            3,5 | 1,3  => 3-1 = 2,   5-3=2
    #    0 0 0 0 0                                  0 0 1 0 0
    #    0 1 0 0 0                                  0 0 0 0 0
    #    0 0 1 0 0                                  0 0 0 0 1
    # row 이전 행렬까지 체스가 놓아져 있기 때문에 row 까지만 계산
    #
    for i in range(row):
        if visited[row] == visited[i] or abs(visited[row] - visited[i]) == abs(row - i):
            return False

    return True


def dfs(k):
    global result

    # k가 N까지 갔다는 의미는 마지막 행까지 퀸이 올바르게 놓여졌다는 의미
    if k == N:
        result += 1
    else:
        for i in range(N):
            # 퀸의 위치를 조절합니다. k행 i열
            visited[k] = i

            # 퀸의 위치가 합당한지 확인합니다.
            if is_ok(k):
                dfs(k+1)


# 몇개의 체스판이 만들어지는지?
result = 0
visited = [0] * N   # 배열의 index를 행으로 사용하고 배열 내부의 값을 열로 사용
dfs(0)  # 가장 위 행렬부터 시작

print(result)
