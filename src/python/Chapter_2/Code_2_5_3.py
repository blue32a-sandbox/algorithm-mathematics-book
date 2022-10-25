# 2.5.3 1以上20以下の整数Nの階乗
N = int(input())
answer = 1

for num in range(1, N + 1):
    answer *= num

print(answer)
