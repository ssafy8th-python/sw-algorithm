X = int(input())
N = int(input())

for _ in range(N):
    money, mount = map(int, input().split())
    X -= money * mount

if X:
    print("No")
else:
    print("Yes")