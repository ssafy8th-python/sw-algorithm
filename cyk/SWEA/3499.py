# 퍼펙트 셔플
import sys
sys.stdin = open("sample_input (6).txt", "r")
'''
3
6
A B C D E F
4
JACK QUEEN KING ACE
5
ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA
'''
T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    cards = input().split()
    size = len(cards)
    if size % 2:
        deck1 = cards[:1+len(cards)//2]
        deck2 = cards[1+len(cards)//2:]
    else:
        deck1 = cards[: len(cards) // 2]
        deck2 = cards[len(cards) // 2:]
    result = []
    i = 0
    while True:
        if deck1:
            elem1 = deck1.pop(0)
            result.append(elem1)
        if deck2:
            elem2 = deck2.pop(0)
            result.append(elem2)
        if len(result) == size:
            break
    print(f'#{tc} ', end='')
    print(*result)