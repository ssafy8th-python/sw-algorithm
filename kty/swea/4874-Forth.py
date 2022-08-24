import sys

sys.stdin = open("input_4874.txt", "r")

def step(nums):
    st = []
    for token in nums:
        if token.isnumeric():
            st.append(token)
        else:
            if token =='.':
                if len(st) == 1:
                    return st[-1]
                else:
                    return 'error'
            if len(st) < 2:
                return 'error'
            right = int(st.pop())
            left = int(st.pop())
            if token == '+':
                st.append(left+right)
            elif token == '-':
                st.append(left-right)
            elif token == '*':
                st.append(left*right)
            elif token == '/':
                st.append(left//right)

T = int(input())
for tc in range(1, T+1):
    nums = input().split()
    print(f'#{tc} {step(nums)}')
    #
    #
    #
    # right = st.pop()
    # left = st.pop()
    # if token == '+':
    #     st.append(int(left)+(int(right)))
    # elif token == '-':
    #     st.append(int(left)-int(right))
    # elif token == '*':
    #     st.append(int(left)*int(right))
    # elif token == '/':
    #     st.append(int(left)/int(right))
