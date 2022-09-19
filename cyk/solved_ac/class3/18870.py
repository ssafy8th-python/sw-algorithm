# 좌표압춝
n = int(input())
ipt = list(map(int, input().split()))
srt_ipt = sorted(list(set(ipt)))

def binary(key):
    start = 0
    end = len(srt_ipt)
    while start <= end:
        middle = (start + end) // 2
        if srt_ipt[middle] == key:
            return middle
        elif srt_ipt[middle] < key:
            start = middle
        else:
            end = middle
for elem in ipt:
    print(binary(elem), end=' ')