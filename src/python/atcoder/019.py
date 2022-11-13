# 019 - Choose Cards 1
n = int(input())
a = list(map(int, input().split()))

rc = a.count(1)
r = rc * (rc - 1) // 2

yc = a.count(2)
y = yc * (yc - 1) // 2

bc = a.count(3)
b = bc * (bc - 1) // 2

print(r + y + b)
