from collections import deque

class Employee:
    def __init__(self, height):
        if height == H:
            self.jobs = deque()
        else:
            self.leftJobs = deque()
            self.rightJobs = deque()

def team_set(index, height):
    if H < height:
        return

    team[index] = Employee(height)
    
    team_set(index * 2, height + 1)
    team_set(index * 2 + 1, height + 1)

def work(day, index, height):
    global result

    if height > H:
        return

    Employee = team[index]

    if height == H and Employee.jobs:
        job = Employee.jobs.popleft()

        if index % 2 == 0:
            team[index // 2].leftJobs.append(job)
        else:
            team[index // 2].rightJobs.append(job)

    elif height < H and day % 2 == 0 and Employee.rightJobs:
        job = Employee.rightJobs.popleft()

        if index == 1:
            result += job
        else:
            if index % 2 == 0:
                team[index // 2].leftJobs.append(job)
            else:
                team[index // 2].rightJobs.append(job)
    elif height < H and day % 2 == 1 and Employee.leftJobs:
        job = Employee.leftJobs.popleft()

        if index == 1:
            result += job
        else:
            if index % 2 == 0:
                team[index // 2].leftJobs.append(job)
            else:
                team[index // 2].rightJobs.append(job)

    work(day, index * 2, height + 1)
    work(day, index * 2 + 1, height + 1)

H, K, R = map(int, input().split())

team = [0] * (2 ** (H + 1))

result = 0

team_set(1, 0)

for i in range(2 ** H, 2 ** (H+1)):
    work_list = list(map(int, input().split()))
    team[i].jobs.extend(work_list)

# 일해라 R일 동안
for i in range(1, R+1):
    work(i, 1, 0)

print(result)