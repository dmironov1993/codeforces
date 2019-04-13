# https://codeforces.com/contest/551/problem/A
# https://codeforces.com/contest/551/submission/52567407

n = int(input())
a = list(map(int, input().split()))

res = []
for i in range(n):
    count = 0
    for j in range(n):
        if a[i] < a[j]:
            count += 1
    res.append(count + 1)
print (*res)
