# 015 - Calculate GCD
a, b = list(map(int, input().split()))

while a >= 1 and b >= 1:
    if a < b:
        b = b % a
    else:
        a = a % b

print(a if a >= 1 else b)
