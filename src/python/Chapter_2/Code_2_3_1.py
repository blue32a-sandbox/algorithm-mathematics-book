# 2.3.1 プログラミングにおける関数の例
cnt = 1000

def func1():
    return 2021

def func2(pos):
    global cnt
    cnt += 1
    return cnt + pos

print(func1()) # 2021
print(func2(500)) # 1501
print(func2(500)) # 1502
