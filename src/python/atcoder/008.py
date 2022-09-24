# 	008 - Brute Force 1
N, S = list(map(int, input().split()))
count = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i + j <= S:
            count += 1

print(count)
