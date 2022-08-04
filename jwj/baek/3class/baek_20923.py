import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
do_queue  = deque()
su_queue = deque()

for _ in range(N):
    do,su = map(int,sys.stdin.readline().split())
    do_queue.append(do)
    su_queue.append(su)

do_check = 0
su_check = 0

do_tmp = deque()
su_tmp = deque()

for m in range(M):

    if m % 2 == 0:
        do_check = do_queue.pop()
        do_tmp.append(do_check)
    else:
        su_check = su_queue.pop()
        su_tmp.append(su_check)

    if not do_queue:
        print("su")
        exit()
    
    if not su_queue:
        print("do")
        exit()

    if (do_check + su_check == 5) and (do_check != 0) and (su_check != 0):

        su_queue.extendleft(do_tmp)
        do_check = 0
        do_tmp = deque()

        su_queue.extendleft(su_tmp)
        su_check = 0
        su_tmp = deque()

    elif (do_check == 5) or (su_check == 5):
        do_queue.extendleft(su_tmp)
        su_check = 0
        su_tmp = deque()

        do_queue.extendleft(do_tmp)
        do_check = 0
        do_tmp = deque()

if len(do_queue) > len(su_queue):
    print("do")
elif len(do_queue) < len(su_queue):
    print("su")
elif len(do_queue) == len(su_queue):
    print("dosu")