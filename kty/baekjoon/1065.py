N = int(input())
cnt = 0
# for i in range(1, N+1):
#     str_i = str(i)
#     if len(str_i) > 2:
#         diff = int(str_i[1])-int(str_i[0])
#         for j in range(2, len(str_i)):
#             if diff != int(str_i[j]) - int(str_i[j - 1]):
#                 break
#             cnt += 1
#     else:
#         cnt += 1
# print(cnt)

for i in range(1, N+1):
    if i < 100:
        cnt += 1
    elif i < 1000:
        if (i % 10) - ((i // 10) % 10) == ((i // 10) % 10) - (i // 100):
            cnt += 1

print(cnt)