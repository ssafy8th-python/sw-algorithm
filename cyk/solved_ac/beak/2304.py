# 창고 다각형
'''
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
mx = 0
for lst in arr:
    if mx < lst[0]:
        mx = lst[0]
check = [0] * (mx + 1)

for lst in arr:
    check[lst[0]] = lst[1]

st = []
for i in range(0, len(check)):
    if not st:  # 처음 시행
        st.append(check[i])
    else:
        if st[-1] < check[i]:   # st의 마지막 값이 현재 인덱스의 값보다 작다면 st에 현재값 추가
            st.append(check[i])

        else:   # 현재 인덱스의 값이 작다면
            if st[-1] <= max(check[i:]):
                st.append(st[-1])

            else:
                st.append(max(check[i:]))

print(sum(st))

