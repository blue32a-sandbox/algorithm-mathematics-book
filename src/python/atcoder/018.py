# 018 - Convenience Store 1
n = int(input())
a = list(map(int, input().split()))

x = a.count(100) * a.count(400)
y = a.count(200) * a.count(300)

print(x + y)
