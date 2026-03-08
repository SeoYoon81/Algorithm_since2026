# 가장 긴 증가하는 부분수열 4

n  = int(input())
num_lst = list(map(int, input().split()))
dp_lst = [(1, -1)]
for idx in range(1, n):
    now_num = num_lst[idx]
    temp_lst = [(0, -1)]+[(dp_lst[i][0], i) for i in range(idx) if num_lst[i]<now_num]
    best_tuple = max(temp_lst)
    dp_lst.append((best_tuple[0] + 1, best_tuple[1]))

max_len, prev_idx = max(dp_lst)
print(max_len)
now_idx = max(range(n), key= lambda i :dp_lst[i][0] )
result_lst = []
while now_idx>=0:
    result_lst.append(num_lst[now_idx])
    now_idx = dp_lst[now_idx][1]
result_lst=result_lst[::-1]
print(*result_lst)