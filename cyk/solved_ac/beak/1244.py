# 스위치 켜기
# 스위치 켜고 끄기
n = int(input())
s = list(map(int, input().split()))
std_num = int(input())
'''
8
0 1 0 1 0 0 0 1
2
1 3
2 3
'''
for _ in range(std_num):
    std = list(map(int, input().split()))
    maximum = min(std[1], n-std[1])
    # print(maximum)# 남학생일때 해당 스위치 상태 변화 => 해당 스위치의 배수의 스위치 상태 변화
    idx_std = std[1]-1
    if std[0] == 1:
        i = 1
        while std[1] * i - 1 < n:
            if s[std[1] * i - 1] == 1:
                s[std[1] * i - 1] = 0
            else:
                s[std[1] * i - 1] = 1
            i += 1
    else:                   # 여학생일때 해당 스위치 상태 변화 => 해당 스위치를 중심으로 대칭을 이루는 큰 범위의 스위치 전부 상태 변화
        if s[idx_std] == 1:
            s[idx_std] = 0
        else:
            s[idx_std] = 1
        for i in range(1, maximum+1):
            if idx_std+i < n and 0 <= idx_std-i and s[idx_std+i] == s[idx_std-i]:
                if s[idx_std+i] == 1:
                    s[idx_std+i], s[idx_std-i] = 0, 0
                else:
                    s[idx_std+i], s[idx_std-i] = 1, 1
            else:
                break
for i in range(0, len(s), 20):  # 20개씩 나눠서 출력
    print(*s[i:i+20])


