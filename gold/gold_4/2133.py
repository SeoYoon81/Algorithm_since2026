# 타일 채우기

n = int(input())
if n %2:
    print(0)
else:
    k = n//2
    tile_lst = [2 for _ in range(n)]
    tile_lst[1] = 3
    result_lst = [1]
    for idx in range(k):
        cnt = sum(result_lst) * 2 + result_lst[-1]
        result_lst.append(cnt)
    print(result_lst[k])