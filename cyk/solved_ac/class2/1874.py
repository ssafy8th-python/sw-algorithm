# 스택수열
# 1~n까지의 수를 스택을 이용하여 입력된 수열과 동일하게 만들어라
'''
8
4
3
6
8
7
5
2
1
'''
# push => + / pop => -

N = int(input())
lst = [int(input()) for _ in range(N)]      # 만들어야 하는 수열 [4, 3, 6, 8, 7, 5, 2, 1]
num_lst = list(range(1, N+1))
st = []
result = []
while True:
    if len(st) > 1 and st == lst:
        result.append(0)
        break
    if st:
        if st[-1] != lst[0]:
            st.append(num_lst[0])
            num_lst.pop(0)
            result.append('+')

    else:
        st.append(num_lst[0])
        num_lst.pop(0)
        result.append('+')

    if st[-1] == lst[0]:
        x = st.pop()
        lst.pop(0)
        result.append('-')

    if not lst:
        break

if 0 in result:
    print('NO')
else:
    for elem in result:
        print(elem)
