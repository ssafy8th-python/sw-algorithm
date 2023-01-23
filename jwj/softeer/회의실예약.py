def print_room(room_num):
    if available_room[room_num]:
        print(f"Room {rooms[room_num][0]}:")
        print(f"{len(available_room[room_num])} available:")
    else:
        print(f"Room {rooms[room_num][0]}:")
        print("Not available")

    for time in available_room[room_num]:
        print(f"{time[0]:02}-{time[1]:02}")


N, M = map(int, input().split())

rooms = {}
for i in range(N):
    room = input()
    rooms[room] = [0] * 18
    rooms[room] += [1]

for i in range(M):
    r, s, t = input().split()
    s = int(s)
    t = int(t)

    for j in range(s, t):
        rooms[r][j] = 1

rooms = sorted(rooms.items(), key=lambda item: item[0])
available_room = []

for room in rooms:
    start_time = 9
    end_time = 9
    time_list = []
    for s in room[1][9:]:
        # s = 0 일 때 가능 한 시간
        if s == 0:
            end_time += 1
        else:
            if start_time != end_time:
                time_list.append((start_time, end_time))
            end_time += 1
            start_time = end_time
    available_room.append(time_list)

for i in range(N-1):
    print_room(i)
    print("-----")

print_room(N-1)
