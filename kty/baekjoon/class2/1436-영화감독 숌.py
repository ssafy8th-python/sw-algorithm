T = int(input())
six = 666
while T > 0:
    if '666' in str(six):
        T -= 1
        if T == 0:
            break
    six += 1

print(six)