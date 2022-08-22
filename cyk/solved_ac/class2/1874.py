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


idx = 0
while idx < N:
    st.append(num_lst[idx])
    result.append('+')

    while True:
        if st[-1] == lst[0]:
            st.pop()
            lst.pop(0)
            result.append('-')
        else:
            break
        if not st:
            break
    idx += 1

if st:      # st에 요소가 남아있으면 no 출력
    print('NO')
else:
    for elem in result:
        print(elem)