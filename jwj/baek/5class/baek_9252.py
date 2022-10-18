s1 = input()
s2 = input()

l1 = len(s1)
l2 = len(s2)

LCS = [[0] * (l1 + 1) for _ in range(l2 + 1)]

for s2_idx in range(l2):
    for s1_idx in range(l1):
        if s1[s1_idx] == s2[s2_idx]:
            LCS[s2_idx+1][s1_idx+1] = LCS[s2_idx][s1_idx] + 1
        else:
            LCS[s2_idx+1][s1_idx+1] = max(LCS[s2_idx+1][s1_idx], LCS[s2_idx][s1_idx+1])

cur = 0

result = ""

if LCS[-1][-1]:
    print(LCS[-1][-1])
    while l1 != 0 and l2 != 0:
        if LCS[l2][l1] == LCS[l2][l1-1]:
            l1 -= 1
        elif LCS[l2][l1] == LCS[l2-1][l1]:
            l2 -= 1
        else:
            if s1[l1-1] == s2[l2-1]:
                result = s1[l1-1] + result
                l1 -= 1
                l2 -= 1
    print(result)
else:
    print(0)
