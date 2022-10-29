# 013 - Divisor Enumeration
import math

N = int(input())
limit = int(math.sqrt(N))
divisors = []

for i in range(1, limit + 1):
    if N % i != 0:
        continue

    divisors.append(i)

    if i != N // i:
        divisors.append(N // i)

for divisor in divisors:
    print(divisor)
