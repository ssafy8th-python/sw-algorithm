# 제로
import sys
input = sys.stdin.readline

T = int(input())
st = []                 # 0일때 넣을 수
for _ in range(T):  
    a = int(input())
    if a :              # 입력이 0가 아니라면 st에 추가 
        st.append(a)
    else:               # 입력이 0라면 pop
        st.pop()

if st:
    print(sum(st))      # 남아있는 요소들의 합 출력
else:
    print(0)            # 요소가 없다면 0 출력