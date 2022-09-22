# 교환
def exc(ipt, cnt):
    global arrLst, mx

    if ipt[0] == '0':
        return

    if cnt == K:
        if int(''.join(ipt)) > mx:
            mx = int(''.join(ipt))
        return

    if int(''.join(ipt)) in arrLst[cnt]:
        return
    else:
        arrLst[cnt].append(int(''.join(ipt)))


    for i in range(size-1):
        for j in range(i+1, size):

            ipt[i], ipt[j] = ipt[j], ipt[i]

            exc(ipt, cnt+1)
            ipt[i], ipt[j] = ipt[j], ipt[i]

ipt, K = input().split()
K = int(K)
size = len(ipt)
mx = 0
arrLst = [[] for _ in range(K)]
exc(list(ipt), 0)
if mx == 0:
    print(-1)
else:
    print(mx)