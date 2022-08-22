# 메모리 복구
'''
2
0011
100
'''
T = int(input())
for tc in range(1,T+1):
    s = list(map(int, input()))
    size = len(s)
    init_lst = [0] * size

    # for i in range(size):
    #     if s[i] == 1:
    #         for j in range(i, size):
    #             init_lst[j] = 1
    cnt = 0
    for i in range(size):
        if s[i] != init_lst[i]:     # 다를때
            if s[i] == 0:
                for j in range(i,size):
                    init_lst[j] = 0
                cnt += 1
            elif s[i] == 1:
                for k in range(i, size):
                    init_lst[k] = 1
                cnt += 1
        if s == init_lst:
            break

    print(f'#{tc} {cnt}')