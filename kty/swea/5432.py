import sys

sys.stdin = open("input_5432.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    still = input()
    stick = 1
    result = 0
    for i in range(1, len(still)):
        if still[i] == '(':
            stick += 1
        else:
            stick -= 1
            if still[i-1] == '(':
                result += stick
            else:
                result += 1
    print(f'#{tc} {result}')