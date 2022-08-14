# 숫자 카드 2
# 각 수가 적힌 숫자 카드를 몇 개 가지고 있는지 공백으로 구분해 출력한다
# 이진탐색으로도 풀어보기
import sys
input = sys.stdin.readline

n1 = int(input())
s1 = list(map(int, input().split()))
n2 = int(input())
s2 = list(map(int, input().split()))

s1_dict = {}

for s1_elem in s1:
    if s1_dict.get(s1_elem) == None:
        s1_dict[s1_elem] = 1
    else:
        s1_dict[s1_elem] += 1

for s2_elem in s2:
    if s1_dict.get(s2_elem):
        print(s1_dict.get(s2_elem), end=" ")
    else:
        print(0, end=" ")