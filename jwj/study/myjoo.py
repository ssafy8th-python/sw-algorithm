numOfCandy = 20
q = []
No = 1
haveCandy = 0

q.append((1, 1, 1))

while haveCandy < numOfCandy:
    No += 1

    person, cnt, my = q.pop(0)

    haveCandy += cnt

    q.append((person, cnt+1, my + cnt))
    q.append((No, 1, 1))

print(person)


