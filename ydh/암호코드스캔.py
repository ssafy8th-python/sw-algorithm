# import sys
# sys.stdin=open("암호코드스캔.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # print(arr)
    newarr = []

    for row in range(1, N) :
        j = M * 4 - 1

        while j >= 56 :
            if newarr[row][j] == 1 and newarr[row - 1][j] == 0 :
                for i in range(8) :
                    a[2] = 1의 갯수를 셈
                    a[1] = 0의 갯수를 셈
                    a[0] = 1의 갯수를 셈
                    k = min(a[0:2])

                    코드하나를 찾아온다.

                암호검증

            else :
                j -= 1