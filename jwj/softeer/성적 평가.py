import heapq

N = int(input())

final_point = [[0, i] for i in range(N)]


def cal_rank(queue):
    rank_arr = [1] * N
    prev_point = heapq.heappop(queue)

    rank = 1
    same = 0

    rank_arr[prev_point[1]] = rank

    for j in range(N-1):
        cur_point = heapq.heappop(queue)
        if cur_point[0] == prev_point[0]:
            rank_arr[cur_point[1]] = rank
            same += 1
        else:
            rank_arr[cur_point[1]] = rank + same + 1
            rank = rank + same + 1
            same = 0
        prev_point = cur_point
    return rank_arr


for i in range(3):
    arr = list(map(int, input().split()))
    q = []
    for j in range(N):
        q.append([-arr[j], j])
        final_point[j][0] -= arr[j]
    heapq.heapify(q)
    result = cal_rank(q)

    print(*result)

heapq.heapify(final_point)

result = cal_rank(final_point)

print(*result)
