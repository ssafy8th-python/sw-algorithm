# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(

T = int(input())
for _ in range(T):
    a = list(input())
    N = len(a)-1
    play = True
    while play:
        for i in range(N):
            if a[i] == '(' and a[i+1] == ')':
                a.pop(i)
                a.pop(i)
                N = len(a) -1
                break
        else:
            print('NO')
            play = False

        if len(a) == 0:
            print('YES')
            play = False


# stack

T = int(input())
for _ in range(T):
    a = list(input())
    st = []
    for i in a:
        if i == '(':
          st.append(i)
        else:
            if st:
                st.pop()
            else:
                st.append(i)
                break

    if st:
        print('NO')
    else:
        print('YES')

