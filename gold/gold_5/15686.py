# 치킨 배달

import sys
input= sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
city = []
for _ in range(n):
    temp_lst = list(map(int, input().split()))
    city.append(temp_lst)

h_lst = []
c_lst = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            h_lst.append((i, j))
        elif city[i][j] == 2:
            c_lst.append((i, j))

len_map = []
for hi, hj in h_lst:
    temp_lst = []
    for ci, cj in c_lst:
        temp_lst.append(abs(hi-ci)+abs(hj-cj))
    len_map.append(temp_lst)

# 도시의 치킨거리 측정
def find_city_len(selected):
    city_len= 0
    for h in range(len(h_lst)):
        min_len = 2*n
        for c in selected:
            min_len = min(min_len, len_map[h][c])
        city_len += min_len
    return city_len

result = 2*n**3

for comb in combinations(range(len(c_lst)), m):
    temp_result = find_city_len(comb)
    result = min(result, temp_result)
print(result)