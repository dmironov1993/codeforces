# https://codeforces.com/contest/979/problem/A

n = int(input())
tot = n + 1
if n == 0:
    print (0)
elif tot % 2 == 0:
    print (tot//2)
else:
    print (tot)
