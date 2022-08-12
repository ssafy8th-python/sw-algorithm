t = int(input())
for i in range(t):
    word = input()
    if word == word[::-1]:
        print('#{} {}'.format(i+1, 1))
    else:
        print('#{} {}'.format(i+1, 0))