# 014 - Factorization
import math

def isprime (N):
    limit = int(math.sqrt(N))
    for i in range(2, limit + 1):
        if N % i == 0:
            return False
    return True

N = int(input())
answer = []

while True:
    if isprime(N):
        answer.append(N)
        break

    for i in range(2, N + 1):
        if isprime(i) == False:
            continue

        if N % i == 0:
            answer.append(i)
            N //= i
            break

print(*answer)
