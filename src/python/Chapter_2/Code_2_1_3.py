# 2.1.3 N個の整数の合計を出力するプログラム
_N = int(input())
A = list(map(int, input().split()))
answer = 0

for num in A:
    answer += num

print(answer)
