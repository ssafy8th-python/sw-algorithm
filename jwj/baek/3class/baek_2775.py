import sys

input = sys.stdin.readline


for test_case in range(int(input())):
    k = int(input())
    n = int(input())

    apt = []
    for num in range(n+1):
        apt.append(num)

    for floor in range(k):
        for room in range(n):
            apt[room+1] = apt[room] + apt[room+1]

    print(apt[-1])