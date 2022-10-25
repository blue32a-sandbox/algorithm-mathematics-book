# 2.5.4 正の整数N以下の素数
N = int(input())

for num in range(2, N + 1):
    isPrime = True

    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        print(num)
