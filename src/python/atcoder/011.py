# 011 - Print Prime Numbers
N = int(input())
primeNumbers = []

for num in range(2, N + 1):
    isPrime = True

    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        primeNumbers.append(num)

print(*primeNumbers)
