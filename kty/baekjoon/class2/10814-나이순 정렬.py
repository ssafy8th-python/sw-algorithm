T = int(input())
a = []
for _ in range(T):
    age, name = map(str, input().split())
    age = int(age)
    a.append((age, name))

a.sort(key=lambda x:x[0])
for i in a:
    print(i[0], i[1])

