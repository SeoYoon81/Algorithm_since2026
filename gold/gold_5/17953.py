# 디저트

n, m = map(int, input().split())
# 디저트 리스트
deserts = []
for _ in range(m):
    now_desert = list(map(int, input().split()))
    deserts.append(now_desert)

# 포인트 리스트 
p_lst = [[deserts[i][0] for i in range(m)]]
for day in range(1, n):
    yesterday = p_lst[day - 1]
    today = []
    for idx in range(m):
        now_point = deserts[idx][day]
        temp = [(yesterday[i] + now_point) for i in range(m) if i != idx] + [yesterday[idx] + now_point//2]
        today.append(max(temp))
    p_lst.append(today)
print(max(p_lst[-1]))