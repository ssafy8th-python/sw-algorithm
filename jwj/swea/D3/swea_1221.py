T = int(input())

for tc in range(1, T+1):
    test_case, num = input().split()
    num = int(num)

    result_dict = {'ZRO' : 0, 'ONE' : 0, 'TWO' : 0, 'THR' : 0, 'FOR' : 0, 'FIV' : 0, 'SIX' : 0, 'SVN' : 0, 'EGT' : 0, 'NIN' : 0}

    num_lst = input().split()

    for n in num_lst:
        result_dict[n] += 1

    print(f'#{tc}')
    for key in result_dict:
        print((key+' ') * result_dict[key] )

