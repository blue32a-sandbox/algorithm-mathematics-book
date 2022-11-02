# 016 - Greatest Common Divisor of N Integers
def greatest_common_divisor(a, b):
    while a >= 1 and b >= 1:
        if a < b:
            b = b % a
        else:
            a = a % b

    return a if a >= 1 else b

n = int(input())
a = list(map(int, input().split()))
answer = a[0]

for i in range(n - 1):
    answer = greatest_common_divisor(answer, a[i + 1])

print(answer)
