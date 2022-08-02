L = int(input())
s = input()
M = 1234567891
r = 31
result = 0
for idx, char in enumerate(s) :
    result += ((ord(char)-96) * (r**idx))

print(result%M)

