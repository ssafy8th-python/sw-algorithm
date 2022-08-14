# 9012 괄호
# 주소: https://www.acmicpc.net/problem/9012

# 제출한 답
t = int(input())

for _ in range(t):
    vps = input()
    flag = True
    stack = []

    for i in vps:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break

    if len(stack) == 0 and flag:
        print('YES')
    else:
        print('NO')


# 다른 답
N = int(input())
for _ in range(N):
    a = input()
    list_a = []
    for i in a:
        if i == "(":
            list_a.append(i)

        if i == ")":
            if len(list_a) == 0 or list_a[-1] != "(":   # flag를 사용하지 않고 그냥 추가해버림
                list_a.append(i)
            else:
                list_a.pop()

    if len(list_a) == 0:                                # 추가한 결과로 스택은 절대로 0이 될 수 없음
        print("YES")
    else:
        print("NO")