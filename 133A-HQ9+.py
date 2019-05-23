# https://codeforces.com/problemset/problem/133/A?locale=ru

a = ['H','Q','9']

p = list(input())
n = len(p)
res = 'NO'
for i in range(n):
    if p[i] in a:
        res = 'YES'
        break
print (res)
