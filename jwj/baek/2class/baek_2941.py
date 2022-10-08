s = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

result = 0
for i in range(len(s)):
    result += 1
    for c in croatia:
        if c[-1] == s[i]:
            if i >= 2 and len(c) == 3 and c[0] == s[i-2] and c[1] == s[i-1]:
                result -= 2
                break
            elif i >= 1 and len(c) == 2 and c[0] == s[i-1]:
                result -= 1
                break

print(result)
