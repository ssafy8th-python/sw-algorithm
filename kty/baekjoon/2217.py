N = int(input())
W = [int(input()) for i in range(N)]

W.sort()
K = [W[i] * (len(W)-i) for i in range(len(W))]
print(max(K))