import sys
sys.stdin = open("GNS_test_input.txt", "r")

dict_s = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

T = int(input())
for tc in range(1, T+1):
    n = input().split()
    # num = n[1]
    s = input().split()
    result_1 = []
    result_2 = []
    dict_r = {dict_s[elem] : elem for elem in dict_s}

    for i in s:
        result_1.append(dict_s[i])
    for j in sorted(result_1):
        result_2.append(dict_r[j])
    print(f'#{tc}')
    print(*result_2)