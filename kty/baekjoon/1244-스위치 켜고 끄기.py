n = int(input())
sw = [-1] + list(map(int, input().split()))
# 켜져 있으면 1, 꺼져 있으면 0
student = int(input())
play = [list(map(int, input().split())) for _ in range(student)]
# 남자 1, 여자 0
for step in play:
    card_num = step[1]
    if step[0] == 1:                # 남학생이면
        for i in range(card_num, len(sw), card_num):
            sw[i] = (sw[i] + 1) % 2
            # sw[i] = 0 if sw[i] else 1

    else:                           # 여학생 이면
        sw[card_num] = (sw[card_num] + 1) % 2
        for k in range(n//2):
            if card_num + k > n or card_num - k < 1:
                break
            if sw[card_num-k] == sw[card_num+k]:
                sw[card_num-k] = (sw[card_num-k] + 1) % 2
                sw[card_num+k] = (sw[card_num+k] + 1) % 2
            else:
                break

for i in range(1, len(sw)):
    print(sw[i], end = ' ')
    if i % 20 == 0:
        print()