n, k = map(int, input().split())

# 여학생 0, 남학생 1

# 성별이 두 개니깐 2차원 배열 만들고 그 안에 1~6학년의 수를 담을 배열 생성
grid = [[0] * 7 for _ in range(2)]

for _ in range(n):
    sex, grade = map(int, input().split())
    if sex:  # 남자면 grid 1번 인덱스 -> 해당하는 학년의 인덱스에 1을 추가
        grid[sex][grade] += 1
    else:   # # 여자면 grid 0번 인덱스 -> 해당하는 학년의 인덱스에 1을 추가
        grid[sex][grade] += 1

room = 0
for i in range(2):
    for j in range(1, 7):
        if grid[i][j] == 0:
            continue                    # 각 배열을 돌면서 해당 학년이 없으면 건너뛰고
        room += grid[i][j] // k         # 해당 성별의 해당 학년의 값을 각 방의 최대 인원수인 k로 나눈 곳을 room에 더하고
        if grid[i][j] % k != 0:         # 나머지가 있을경우 1을더 더해준다.
            room += 1
print(room)