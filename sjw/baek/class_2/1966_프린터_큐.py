# 1966 프린터 큐
# 주소: https://www.acmicpc.net/problem/1966

# 제출한 답
for _ in range(int(input())):
    n, idx = map(int, input().split())    # n: 프린트 수 m: 대상 인덱스
    printer = list(map(int, input().split()))   # 우선순위

    # 대상의 앞이 append(pop(0)) 되면 m -= 1
    # 대상의 앞이 프린트(pop(0)) 되면 m -= 1, cnt += 1
    # 대상 인덱스가 0이고 뒤에 우선 순위가 높은게 없다면 현재 cnt 프린트 브레이크
    # 대상의 인덱스가 0이고 뒤에 우선 순위가 높은게 있다면 m = len(printer - 1)

    cnt = 0

    while len(printer) > 0:
        if idx > 0:
            if max(printer) == printer[0]:
                printer.pop(0)
                cnt += 1
                idx -= 1
            else:
                printer.append(printer.pop(0))
                idx -= 1
        else:
            if max(printer) == printer[0]:
                cnt += 1
                print(cnt)
                break
            else:
                printer.append(printer.pop(0))
                idx = len(printer) - 1
