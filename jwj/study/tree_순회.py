'''
정점 번호 V : 1~(E+1)
간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5
'''


def find_root():
    for i in range(1, V + 1):
        if parent[i] == 0:  # 부모가 없으면 root
            return i
    return 0    # root를 못찾았을 때


def preorder(n):
    if n:
        print(n)
        preorder(ch1[n])
        preorder(ch2[n])


E = int(input())
V = E + 1

arr = list(map(int, input().split()))

# 부모 인덱스로 자시 번호 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)

# 자식을 인덱스로 부모 번호 저장, 루트나 조상을 찾기 위해 사용
parent = [0] * (V + 1)

root = 1

for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i+1]

    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

    parent[c] = p

preorder(root)

print('root :', find_root())

# 배열 인덱스로 접근
#
# def pre(n):
#     if n <= size:
#         print(tree[n])
#         pre(2 * n)
#         pre(2 * n + 1)
#
#
# tree = [0, 'A', 'B', 'C', 'D', 'E', 'F']
# size = len(tree) - 1
# pre(1)
