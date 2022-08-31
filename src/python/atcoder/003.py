# 003 - Sum of N Integers
_N = int(input())
A = list(map(int, input().split()))
answer = 0

for num in A:
    answer += num

print(answer)
