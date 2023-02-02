# nums = list(map(int, input().split()))
#
# for i in range(1, 1000001):
#     tmp = 0
#
#     for num in nums:
#         if i % num == 0:
#             tmp += 1
#
#     if tmp >= 3:
#         break
#
# print(i)

# 최소 공배수를 이용해 문제 해결하기
def gcd(a, b):
    while b > 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    return a * b // gcd(a, b)


nums = list(map(int, input().split()))

ans = 1000000

for i in range(3):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            ans = min(ans, lcm(lcm(nums[i], nums[j]), nums[k]))

print(ans)
