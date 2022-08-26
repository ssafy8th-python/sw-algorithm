import sys

sys.stdin = open("input_1265.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    moc = n // m
    na = n % m
    print(f'#{tc} {(moc**(m-na))*((moc+1)**na)}')
