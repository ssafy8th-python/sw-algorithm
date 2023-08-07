def solution(s, skip, index):
    answer = ''
    count = 0

    for c in s:
        num = ord(c)
        while True:
            num += 1
            if num > ord('z'):
                num = ord('a')
            if chr(num) not in skip:
                print('hi')
                count += 1
            if index == count:
                answer += chr(num)
                break

    return answer


tc = ['aukks', 'wbqd', 5]

print(solution(tc[0], tc[1], tc[2]))