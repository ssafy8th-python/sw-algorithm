# 작업 순서
# 방향성을 가진 간선
# import sys
# sys.stdin = open("sample_input (7).txt", "r")

def order(start_lst):
    st = []
    for elem in start_lst:
        st.append(elem)
    start = st.pop()
    print(start, end=' ')
    start = st.pop()
    while st:
        for w in lst[start]:
            if not visited[w]:
                print(w, end=' ')
                st.append(start)
                start = w
                visited[start] = True
                break
        else:
            start = st.pop()

for tc in range(1, 2):
    V, E = map(int, input().split())
    lst = [[] for _ in range(V+1)]
    ipt = list(map(int, input().split()))
    start = ipt[0]
    start_lst = []

    for i in range(0, E*2, 2):
        lst[ipt[i+1]].append(ipt[i])
        start_lst.append(ipt[i+1])
    visited = [False] * (len(lst))
    print(lst)
    start_lst = list(set(list(range(1,E+1)))-set(start_lst))
    print(start_lst)
    order(start_lst)

    print()