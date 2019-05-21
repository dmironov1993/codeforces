# https://codeforces.com/problemset/problem/1003/A?locale=en

n = int(input())
a = list(map(int, input().split()))

dct = {}
for i in range(n):
    if a[i] not in dct.keys():
        dct[a[i]] = 1
    else:
        dct[a[i]] += 1
print (max(dct.values()))
