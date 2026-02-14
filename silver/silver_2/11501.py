#주식
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    price_lst = list(map(int, input().split()))
    max_price = 0 
    total = 0
    for i in range(n -1, -1, -1):
        now_price = price_lst[i]
        if now_price > max_price:
            max_price = now_price
        else:
            total += max_price - now_price
    print(total)
