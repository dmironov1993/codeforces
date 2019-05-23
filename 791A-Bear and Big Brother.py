# https://codeforces.com/problemset/problem/791/A

from math import log, floor
a,b = [*map(int, input().split())]
print (floor(log(b/a)/log(3/2) + 1))
