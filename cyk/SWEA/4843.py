

def bubblesort(s):
     for i in range(len(s) - 1, -1, -1):
         for j in range(0, i):
             if s[j] > s[j + 1]:
                 s[j], s[j + 1] = s[j + 1], s[j]
     return s

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    s = list(map(int, input().split()))

    print(f'#{tc}', end=' ')
    for i in range(0,5):
        print(bubblesort(s)[n-i-1], bubblesort(s)[i], end=' ')
    print()
