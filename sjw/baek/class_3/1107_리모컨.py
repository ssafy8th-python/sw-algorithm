# 1107 리모컨
# 주소: https://www.acmicpc.net/problem/1107

# 제출한 답
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
if m:
    broken = input().split()
else:
    broken = []

a = -1
b = abs(100 - n)
while a <= 1000000:
    a += 1
    if b <= len(str(a)) + abs(n - a):
        continue
    for i in str(a):
        if i in broken:
            break
    else:
        b = min(b, len(str(a)) + abs(n - a))


print(b)



# 다른 답
def find_upper_btm_idx(avail, kn):
    for i in range(len(avail)):
        if kn < avail[i]:
            return i
    return None


def find_lower_top_idx(avail, kn):
    for i in range(1, len(avail)+1):
        if kn > avail[-i]:
            return len(avail)-i
    return None


def find_upper(avail_btn, i, ns, base):
    if i < 0:
        if avail_btn[0] != 0:
            return f'{avail_btn[0]}' + base
        elif len(avail_btn) >= 2:
            return f'{avail_btn[1]}' + base
        else:
            return '999'+base

    upper_btm = find_upper_btm_idx(avail_btn, int(ns[i]))
    if upper_btm is None:
        new_base = base[:i] + f'{avail_btn[0]}' + base[i+1:]
        return find_upper(avail_btn, i-1, ns, new_base)
    else:
        return base[:i] + f'{avail_btn[upper_btm]}' + base[i+1:]


def find_lower(avail_btn, i, ns, base):
    if i < 0:
        if base[1:] == '':
            return '9'*len(ns)
        return base[1:]
    lower_top = find_lower_top_idx(avail_btn, int(ns[i]))
    if lower_top is None:
        new_base = base[:i] + f'{avail_btn[-1]}' + base[i+1:]
        return find_lower(avail_btn, i-1, ns, new_base)
    else:
        return base[:i] + f'{avail_btn[lower_top]}' + base[i+1:]


n = int(input())
m = int(input())
broken_btn = []
if m != 0:
    broken_btn = [int(x) for x in input().split()]
avail_btn = [x for x in range(10) if x not in broken_btn]
ns = f'{n}'
l = len(ns)

if n == 100:
    print(0)
elif m == 0:
    print(min(l, abs(n-100)))
elif m == 10:
    print(abs(n-100))
else:
    diff_i = l
    for i in range(l):
        if int(ns[i]) not in avail_btn:
            diff_i = i
            break
    if diff_i == l:
        print(min(l, abs(n-100)))
    else:
        upper_base = ns[:diff_i+1] + f'{avail_btn[0]}' * (l-diff_i-1)
        upper_bound = int(find_upper(avail_btn, diff_i, ns, upper_base))
        upper_bound_r = abs(upper_bound - n) + len(f'{upper_bound}')
        lower_base = ns[:diff_i+1] + f'{avail_btn[-1]}' * (l-diff_i-1)
        lower_bound = int(find_lower(avail_btn, diff_i, ns, lower_base))
        lower_bound_r = abs(lower_bound - n) + len(f'{lower_bound}')
        r = min([upper_bound_r, lower_bound_r, abs(n-100)])
        print(r)