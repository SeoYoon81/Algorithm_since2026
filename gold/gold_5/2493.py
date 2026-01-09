#탑
from collections import deque
n = int(input())
tower_lst = list(map(int, input().split()))

show_stack = []
result =[0] * n

for idx in range(n):
    height = tower_lst[idx]
    #작은 놈 제거
    while show_stack and show_stack[-1][1] < height:
        show_stack.pop()
    # result 추가
    if show_stack:
        result[idx] = show_stack[-1][0] + 1
    # stack에 현재 tower 추가
    show_stack.append((idx, height))
print(*result)