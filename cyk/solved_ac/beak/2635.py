# 수 이어가기
# 첫번째 수로 양의 정수
# 두번째 수는 양의 정수 중에서 하나 선택
# 세번째 이후에 나오는 모든 수는 앞의 앞의 수에서 앞의 수를 빼서 만든다
# 음의 정수가 만들어지면 버리고 더 이상 만들지 않는다

def check(lst):     # 규칙 시행 함수
    if lst[-1] < 0:
        lst.pop()
        return lst
    else:
        elem = lst[-2]-lst[-1]
        lst.append(elem)
        return check(lst)


num = int(input())
i = 0
size = []

while True:                 # 첫번째 수
    lst = [num]
    lst.append(num-i)       # 두번째 수
    check_lst = check(lst)  # 함수 호출
    size.append(len(check_lst))
    if len(size) >= 2 and size[-1] < size[-2]:
        print(result_size)
        print(*result)
        break
    result = check_lst
    result_size = size[-1]
    i += 1
