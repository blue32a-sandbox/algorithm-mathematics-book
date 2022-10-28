# 012 - Primality Test
import math

def isprime (N):
    limit = int(math.sqrt(N))
    for i in range(2, limit + 1):
        if N % i == 0:
            return False
    return True

N = int(input())

print("Yes" if isprime(N) else "No")
