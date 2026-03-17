#CCW
# 복소평면으로 접근
o1, o2 = map(int, input().split())
a,b = map(int, input().split())
a1, a2 = a-o1, b-o2
x,y = map(int, input().split())
b1, b2 = x-o1, y-o2
i = a1*b2 - a2*b1
if i>0:
    print(1)
elif i==0:
    print(0)
else:
    print(-1)