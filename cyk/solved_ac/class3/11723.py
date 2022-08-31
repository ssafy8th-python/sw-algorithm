# 집합
# 비트마스킹 ?
# add x: S에 x를 추가 (1 ≤ x ≤ 20) S에 x가 이미 있는 경우 연산을 무시
# remove x: S에서 x를 제거 (1 ≤ x ≤ 20) S에 x가 없는 경우 연산을 무시
# check x: S에 x가 있으면 1을, 없으면 0을 출력 (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거, 없으면 x를 추가. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.
#

import sys
input = sys.stdin.readline

S = set()  # 비어있는 공집합

def add(x):
    S.add(x)
def remove(x):
    if x in S:
        S.remove(x)
def check(x):
    if x in S:
        return 1
    return 0

def toggle(x):
    if x in S:
        S.remove(x)
    else:
        S.add(x)

def all():
    S = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}    #range 문자열 map하면 시간초과
    return S
def empty():
    S = set()
    return S


n = int(input())

for tc in range(1, n+1):
    cmd = input().split()

    if cmd[0] == 'add':
        add(cmd[1])
    elif cmd[0] == 'remove':
        remove(cmd[1])
    elif cmd[0] == 'check':
        print(check(cmd[1]))
    elif cmd[0] == 'toggle':
        toggle(cmd[1])
    elif cmd[0] == 'all':
        S = all()

    elif cmd[0] == 'empty':
        S = empty()

