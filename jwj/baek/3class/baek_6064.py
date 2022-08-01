
for test_case in range(int(input())):
    M, N, x, y = map(int, input().split())
    

    while True:
        
        # x는 현재 해 
        # 현재 해 % N 은 y 가 되었을 때 정답
        # N 과 y 가 같을 때 y%N == 0이 되기 때문에 x%N == y라는 식은 합리적이지 않음
        if x%N == y%N:
            print(x)
            break

        if x > M * N:   # x가 M * N의 범위를 벗어나면 -1 출력
            print(-1)
            break

        # x + M 은 어차피 x이기 때문에 해를 고정해줌
        x += M  

# M  N  x y
# 10 12 3 9

# M  N  x y
# 12 6  5 6

# 33