# 3.1.3 約数をすべて出力するプログラム
import math

N = int(input())
limit = int(math.sqrt(N))
divisors = []

for i in range(1, limit + 1):
    if N % i != 0:
        continue

    # iで割り切れる場合、iは約数
    divisors.append(i)

    if i != N // i:
        # N/iも約数
        divisors.append(N // i)

divisors.sort()
print(divisors)
