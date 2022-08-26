# 오큰수
'''
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

4
3 5 2 7
'''

N = int(input())
s = list(map(int, input().split())) # [3, 5, 2, 7]
result = []                         # 자신보다 크면서 오른쪽에 있는 수중에 가장 인접한 수 모은 결과
temp = []                           # 값이 temp에 있는 수보다 크다면 temp에 들어있는 값 pop 한 후 값을 append

for i in range(len(s)-1, -1, -1):  # 뒤에서부터 시작
    if not temp:
        result.append(-1)          # 마지막 값은 비교대상이 없기 때문에 -1 결과리스트에 넣음
        temp.append(s[i])          # temp에 값 추가
    else:
        if temp[-1] > s[i]:         # temp의 끝 값이 크다면
            result.append(temp[-1]) # temp의 값을 결과에 넣고
            temp.append(s[i])       # temp에 추가
        else:
            while temp and temp[-1] <= s[i]: # temp의 값이 작다면 큰 수가 나올때까지 pop
                temp.pop()
            if not temp:            # temp가 비었을 때
                result.append(-1)   # 자신보다 큰 값이 없다는 뜻이므로 결과에 -1을 넣고
                temp.append(s[i])   # temp에 자신 추가

            else:                   # pop을 진행한 후 큰수가 나왔다면
                result.append(temp[-1]) # 큰수를 결과값에 넣고
                temp.append(s[i])   # temp에 값 추가


print(*result[::-1])                # 뒤에서 시행했으므로 뒤집어서 출력
# 5 7 7 -1






