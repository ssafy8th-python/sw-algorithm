# 배수 스위치
'''
YYYNYYYNYYYNYYNYYYYN

4
'''

light = list(input())
cnt = 0
for i in range(1, len(light)+1):
    if light[i-1] == 'Y':
        mult = 1
        cnt += 1
        while mult*i <= len(light):
            if light[mult*i-1] == 'Y':
                light[mult * i-1] = 'N'
            else:
                light[mult * i-1] = 'Y'
            mult += 1
print(cnt)