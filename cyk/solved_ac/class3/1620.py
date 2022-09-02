# 나는야 포켓몬 마스터 이다솜
# 첫째줄 포켓몬 개수 N개 맞춰야하는 문제의 개수 M개 
# N개의 줄에 포켓몬의 번호가 1번~N번 
# 문자 -> 숫자, 숫자 -> 문자
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
pocket = {}
for i in range(1,1+N):
    ipt = input().rstrip()
    pocket[str(i)] = ipt
    pocket[ipt] = str(i)

for i in range(M):
    print(pocket.get(input().rstrip()))