n, k = map(int, input().split())
result =[]
count_1_result =[]
count_2_result =[]
for _ in range(n):
    a = list(input())
    result.append(a)

for x in range(0, k-7):
    for y in range(0,n-7) :
        count_1 = 0
        count_2 = 0
        slice_chess =[]
        for i in range(y, y+8) :
            slice_chess.append(result[i][x:x+8])
        for idx_1, lst in enumerate(slice_chess):
            if not(idx_1 % 2) :
                for idx_2, elem in enumerate(lst) :
                    if idx_2 % 2 and elem == 'B':
                        count_1 += 1
                    if not(idx_2 % 2) and elem == 'W':
                        count_1 += 1 
            else :
                for idx_2 ,elem in enumerate(lst):
                    if idx_2 % 2 and elem == 'W' :
                        count_1 += 1
                    if not(idx_2 % 2) and elem == 'B':
                        count_1 += 1

        for idx_1, lst in enumerate(slice_chess):
            if not(idx_1 % 2) :
                for idx_2, elem in enumerate(lst) :
                    if idx_2 % 2 and elem == 'W':
                        count_2 += 1
                    if not(idx_2 % 2) and elem == 'B':
                        count_2 += 1 
            else :
                for idx_2 ,elem in enumerate(lst):
                    if idx_2 % 2 and elem == 'B' :
                        count_2 += 1
                    if not(idx_2 % 2) and elem == 'W':
                        count_2 += 1
                                                        
        count_1_result.append(count_1)
        count_2_result.append(count_2)
print(min(min(count_1_result), min(count_2_result)))    

    