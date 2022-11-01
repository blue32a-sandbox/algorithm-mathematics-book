# 3.2.1 最大公約数を求めるプログラム

def greatest_common_divisor(a, b):
    answer = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            answer = i

    return answer

a, b = list(map(int, input().split()))
print(greatest_common_divisor(a, b))
