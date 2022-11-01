# 3.2.2 ユークリッドの互除法で最大公約数を求めるプログラム

def greatest_common_divisor(a, b):
    while a >= 1 and b >= 1:
        if a < b:
            b = b % a
        else:
            a = a % b

    return a if a >= 1 else b

a, b = list(map(int, input().split()))
print(greatest_common_divisor(a, b))
