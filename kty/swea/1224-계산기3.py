import sys

sys.stdin = open("input_1224.txt", "r")

def step1(nums):
    st = []
    word = []

    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    osp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}

    for num in nums:
        if num.isnumeric():
            word.append(num)
        elif num == ')':
            while st and st[-1] != '(':
                word.append(st.pop())
            st.pop()

        else:
            if not st:
                st.append(num)
            elif osp[num] > isp[st[-1]]:
                st.append(num)
            else:
                while st and isp[st[-1]] >= osp[num]:
                    word.append(st.pop())
                st.append(num)
    while st:
        word.append(st.pop())

    return ''.join(word)

def step2(nums):
    st = []
    for num in nums:
        if num.isdecimal():
            st.append(num)
        else:
            right = int(st.pop())
            left = int(st.pop())
            if num == '+':
                st.append(left+right)
            elif num == '-':
                st.append(left-right)
            elif num == '*':
                st.append(left*right)
            elif num == '/':
                st.append(left/right)
    return st[-1]

T = 10
for tc in range(1, T + 1):
    n = int(input())
    nums = input()
    result = step1(nums)
    print(f'#{tc} {step2(result)}')