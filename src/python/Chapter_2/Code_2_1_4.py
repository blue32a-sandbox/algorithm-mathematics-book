# 2.1.4 10進数を2進数に変換するプログラム
N = int(input())
x = N
answer = ""

while x >= 1:
    c = "0" if x % 2 == 0 else "1"
    answer = c + answer
    x = x // 2

print(answer)
