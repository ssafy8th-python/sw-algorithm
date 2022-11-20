N = int(input())

tier = {'B': 1, 'S': 2, 'G': 3, 'P': 4, 'D': 5}

problems = list(input().split())

cur = problems[0]

p1 = 0
p2 = 0

for i in range(1, N):
    cur_t = cur[0]
    next_t = problems[i][0]

    if tier[cur_t] > tier[next_t]:
        p1 = i
        break
    elif tier[cur_t] == tier[next_t]:
        cur_n = int(cur[1:])
        next_n = int(problems[i][1:])
        if cur_n < next_n:
            p1 = i
            break

    cur = problems[i]

if p1:
    cur = problems[N-1]

    for i in range(N-1, p1-2, -1):
        cur_t = cur[0]
        next_t = problems[i][0]

        if tier[cur_t] < tier[next_t]:
            p2 = i
            break
        elif tier[cur_t] == tier[next_t]:
            cur_n = int(cur[1:])
            next_n = int(problems[i][1:])
            if cur_n > next_n:
                p2 = i
                break

        cur = problems[i]

if p1 or p2:
    print('KO')
    print(problems[p2+1], problems[p1-1])
else:
    print('OK')
