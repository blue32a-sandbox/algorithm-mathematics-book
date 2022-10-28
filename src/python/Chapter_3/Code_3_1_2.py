# 3.1.2 高速な素数判定を行うプログラム
import math

def isprime (N):
    limit = int(math.sqrt(N))
    for i in range(2, limit + 1):
        if N % i == 0:
            return False
    return True

N = int(input())

if isprime(N):
    print("is prime")
else:
    print("is not prime")
