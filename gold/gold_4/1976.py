# 여행가자
import sys
input = sys.stdin.readline

n = int(input())   # 도시의 수
m = int(input())   # 계획의 수

map_dict = {}
for i in range(1, n + 1):
    now_lst = [0] + list(map(int, input().split()))
    map_dict[i] = [ j for j in range(1, n + 1) if now_lst[j]==1]
print(map_dict)