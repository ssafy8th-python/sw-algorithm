alphabet = input()

result = 0
for a in alphabet:
    tmp = ord(a)
    if ord('A') <= tmp <= ord('C'):
        result += 3
    elif ord('D') <= tmp <= ord('F'):
        result += 4
    elif ord('G') <= tmp <= ord('I'):
        result += 5
    elif ord('J') <= tmp <= ord('L'):
        result += 6
    elif ord('M') <= tmp <= ord('O'):
        result += 7

    elif ord('P') <= tmp <= ord('S'):
        result += 8

    elif ord('T') <= tmp <= ord('V'):
        result += 9
    elif ord('W') <= tmp <= ord('Z'):
        result += 10

print(result)