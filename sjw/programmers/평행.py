# 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.
#
# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.
#
# 제한사항
# 0 ≤ dots의 원소 ≤ 100
# dots의 길이 = 4
# dots의 원소의 길이 = 2
# dots의 원소는 [x, y] 형태이며 x, y는 정수입니다.
# 서로 다른 두개 이상의 점이 겹치는 경우는 없습니다.
# 두 직선이 겹치는 경우(일치하는 경우)에도 1을 return 해주세요.
# 임의의 두 점을 이은 직선이 x축 또는 y축과 평행한 경우는 주어지지 않습니다.

for dots in [[[1, 4], [9, 2], [3, 8], [11, 6]], [[3, 5], [4, 1], [2, 4], [5, 10]]]:
    answer = 0


    def f(i):
        global answer
        if i == 4:
            a = (dots[0][0] - dots[1][0], dots[0][1] - dots[1][1])
            b = (dots[2][0] - dots[3][0], dots[2][1] - dots[3][1])
            if a == b:
                answer = 1
        else:
            for j in range(i, 4):
                dots[i], dots[j] = dots[j], dots[i]
                f(i + 1)
                dots[i], dots[j] = dots[j], dots[i]
        return 0
    f(0)
    print(answer)