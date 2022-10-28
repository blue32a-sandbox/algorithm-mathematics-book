# 3.1.1 素数判定を行うプログラム
def isprime (N):
    for i in range(2, N):
        if N % i == 0:
            return False
    return True

N = int(input())

if isprime(N):
    print("is prime")
else:
    print("is not prime")
