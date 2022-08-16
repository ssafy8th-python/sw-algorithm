while True:
    a = input()
    if a == '.': # end point
        break
    bracket = []
    for elem in a:
        if elem == ')' or elem == '(' or elem == ']' or elem == '[':
            bracket.append(elem) # 괄호만 선별한 리스트 생성
    i = 0
    while len(bracket) > 1 and i < len(bracket)-1: # 괄호 리스트의 개수가 2개 이상이고 인덱스 번호가 괄호길이를 벗어나지 않을때까지
        if bracket[i]+bracket[i+1] == '()' or bracket[i]+bracket[i+1] == '[]': #만약 연속된 두개의 요소가 '()'이거나 '[]'이면
            bracket.pop(i)#두 요소 제거
            bracket.pop(i)
            i = 0 # 인덱스 0으로 초기화
        else:
            i += 1 #조건이 맞지 않으면 다음 인덱스 판별
    if bracket:
        print('no') # 괄호가 짝이 맞지 않는다면 no 출력
    else:
        print('yes') # 짝이 맞아 전부 삭제되었다면 yes 출력