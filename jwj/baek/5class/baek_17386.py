def is_cross(p11, p12, p21, p22, p31, p32, p41, p42):

    f1 = (p21 - p11) * (p32 - p12) - (p31 - p11) * (p22 - p12)
    f2 = (p21 - p11) * (p42 - p12) - (p41 - p11) * (p22 - p12)

    if f1 * f2 < 0:
        return True
    else:
        return False


p11, p12, p21, p22 = map(int, input().split())

p31, p32, p41, p42 = map(int, input().split())

result1 = is_cross(p11, p12, p21, p22, p31, p32, p41, p42)
result2 = is_cross(p31, p32, p41, p42, p11, p12, p21, p22)

if result1 and result2:
    print(1)
else:
    print(0)