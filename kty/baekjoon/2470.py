N = int(input())
arr = list(map(int, input().split()))
arr.sort()

st = 0
ed = N-1

minV = 2000000000
mix_st = 0
mix_ed = 0
while st != ed:
    sum = arr[st] + arr[ed]
    mix = abs(sum)
    if mix < minV:
        minV = mix
        mix_st = st
        mix_ed = ed

    if sum > 0:
        ed -= 1

    else:
        st += 1

print(arr[mix_st], arr[mix_ed])



