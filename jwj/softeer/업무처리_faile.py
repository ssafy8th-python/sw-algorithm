from collections import deque

# 말단 직원에게 업무 할당
def assign(team, task, height):
    task_index = 0

    for i in range(2 ** height, 2 ** (height + 1)):
        if not team[i]:
            team[i] = task[task_index].popleft()
        task_index += 1


H, K, R = map(int, input().split())

team = [0] * (2 ** (H + 1))

task = [[] for _ in range(2 ** H)]
for i in range(2 ** H):
    task[i] = deque(map(int, input().split()))

# 말단 직원에게 업무 할당
assign(team, task, H)

result = 0

# 업무 올리기
for i in range(2, R+1):

    # 팀원들 전체 탐색
    for j in range(1, 2 ** H):
        # 홀수 번째 날에는 왼쪽 부하직원이 올린 업무를 올리기
        if i % 2:
            if not team[j]:
                team[j] = team[j * 2]
                team[j * 2] = 0
        # 짝수 번째 날에는 오른쪽 부하직원이 올린 업무를 올리기
        else:
            if not team[j]:
                team[j] = team[j * 2 + 1]
                team[j * 2 + 1] = 0
    result += team[1]
    team[1] = 0

    # 말단 직원에게 업무 할당하기
    assign(team, task, H)

print(result)
