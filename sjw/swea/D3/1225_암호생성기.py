# 1225 암호생성기
# 주소: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE&problemTitle=1225&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

for _ in range(10):
    n = int(input())

    num_lst = list(map(int, input().split()))

    while num_lst[7] > 0:
        for i in range(5):
            num_lst[0] -= (i + 1)
            if num_lst[0] <= 0:
                num_lst[0] = 0
                num_lst.append(num_lst.pop(0))
                break
            else:
                num_lst.append(num_lst.pop(0))

    print(f'#{n}', end=' ')
    print(*num_lst)