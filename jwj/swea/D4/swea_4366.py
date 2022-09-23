T = int(input())


def cal():
    for i in range(bi_len):
        bi = binary[:]
        bi[i] = str((int(bi[i]) + 1) % 2)
        bi_set.add(int(''.join(bi), 2))

    for i in range(tri_len):
        for j in range(1, 3):
            t = tri[:]
            t[i] = str((int(t[i]) + j) % 3)
            tri_set.add(int(''.join(t), 3))

    return bi_set & tri_set


for test_case in range(1, T+1):

    binary = list(input())
    tri = list(input())
    bi_len = len(binary)
    tri_len = len(tri)

    bi_set = set()
    tri_set = set()

    print(f'#{test_case} {cal().pop()}')
