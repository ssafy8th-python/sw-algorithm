T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    people = list(map(int, input().split()))
    people.sort()
    bread = 0

    time = 0

    while people:
        time += M
        bread += K

        if time > people[0]:
            time -= M
            bread -= K
            if bread < 1:
                result = 'Impossible'
                break
            else:
                bread -= 1
                people.pop(0)
    else:
        result = 'Possible'

    print(f'#{tc} {result}')
