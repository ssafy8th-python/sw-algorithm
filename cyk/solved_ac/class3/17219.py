# 비밀번호 찾기
# 저장된 사이트 주소의 수 N (1~100000)
# 비밀번호를 찾으려는 사이트 주소의 수 M (1~100000)
'''
16 4
noj.am IU
acmicpc.net UAENA
startlink.io THEKINGOD
google.com ZEZE
nate.com VOICEMAIL
naver.com REDQUEEN
daum.net MODERNTIMES
utube.com BLACKOUT
zum.com LASTFANTASY
dreamwiz.com RAINDROP
hanyang.ac.kr SOMEDAY
dhlottery.co.kr BOO
duksoo.hs.kr HAVANA
hanyang-u.ms.kr OBLIVIATE
yd.es.kr LOVEATTACK
mcc.hanyang.ac.kr ADREAMER
startlink.io
acmicpc.net
noj.am
mcc.hanyang.ac.kr
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
sites = {}
for _ in range(N):
    site, password = input().split()
    sites[site] = password
for _ in range(M):
    ipt = input()
    print(sites[ipt.rstrip()])

