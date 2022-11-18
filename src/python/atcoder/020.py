# 020 - Choose Cards 2
# Pythonで提出するとTLEになるが、PyPy3で提出するとACになる
n = int(input())
a = list(map(int, input().split()))
answer = 0

for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            for l in range(k + 1, n):
                for m in range(l + 1, n):
                    if a[i] + a[j] + a[k] + a[l] + a[m] == 1000:
                        answer += 1

print(answer)
