import sys
sys.stdin = open("input (2).txt", "r")

for tc in range(1, 11):
    N, s = input().split()
    s = list(map(int, s))
    st = []
    for elem in s:
        if st:
            if elem == st[-1]:
                st.pop()
            else:
                st.append(elem)
        else:
            st.append(elem)
    print(f'#{tc} ', end="")
    print(''.join(list(map(str, st))))
