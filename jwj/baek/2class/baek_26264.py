n = int(input())

str = input()

security = 0
bigdata = 0

for s in str:
    if s == 's':
        security += 1

    if s == 'b':
        bigdata += 1

if security > bigdata:
    print('security!')
elif security == bigdata:
    print('bigdata? security!')
else:
    print('bigdata?')
