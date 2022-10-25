# 010 - Factorial
N = int(input())
answer = 1

for num in range(1, N + 1):
    answer *= num

print(answer)
