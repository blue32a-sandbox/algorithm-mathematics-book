# 007 - Number of Multiples 1
N, X, Y = list(map(int, input().split()))
count = 0

for num in range(N):
    num += 1
    if num % X == 0 or num % Y == 0:
        count += 1

print(count)
