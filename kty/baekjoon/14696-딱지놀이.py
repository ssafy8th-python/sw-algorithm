n = int(input())
game = [list(map(int, input().split())) for _ in range(n*2)]

for i in range(0, len(game), 2):
    a = [0] * 5       # 1 ~ 4 딱지 개수를 담을 리스트를 만듬
    b = [0] * 5
    for a_dda in game[i][1:]:   # 딱지 모양대로 해당 리스트의 인덱스에 1씩 추가
        a[a_dda] += 1
    for b_dda in game[i+1][1:]:
        b[b_dda] += 1

    for j in range(4, 0, -1):   # 별(4) 가 제일 쎄니깐 뒤에서 부터 봄
        if a[j] == b[j]:        # 제일 쎈 모양의 개수가 같으면 다음 쎈거 봄
            continue
        elif a[j] > b[j]:
            print('A')
            break
        else:
            print('B')
            break
    else:
        print('D')
