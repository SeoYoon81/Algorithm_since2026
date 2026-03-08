#예산

import sys
input= sys.stdin.readline

n = int(input())

request_lst = list(map(int, input().split()))
total_money = int(input())

if sum(request_lst)>total_money:
    request_lst.sort()
    new_lst = [request_lst[0]] +[request_lst[i]- request_lst[i-1] for i in range(1, n)]
    result = 0
    idx = 0
    while total_money>=new_lst[idx]*(n-idx):
        now_price = new_lst[idx]
        result += now_price
        total_money -= now_price * (n-idx)
        idx += 1    
    #나머지는 균등하게 뿌려야지
    result += total_money//(n-idx)
    print(result)

else:print(max(request_lst))