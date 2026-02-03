# 에디터

import sys
input = sys.stdin.readline

left = list(input().strip())
right = []

m = int(input())
for _ in range(m):
    order = input().strip()
    if order == 'L':
        if left:
            right.append(left.pop())
    elif order == 'D':
        if right:
            left.append(right.pop())
    elif order == 'B':
        if left:
            left.pop()
    else:
        left.append(order[2])

print(''.join(left + right[::-1]))