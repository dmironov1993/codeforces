# https://codeforces.com/contest/1153/problem/A

import math

def distance(a,b):
    return abs(a-b)

n, t = tuple(map(int, input().split()))

s, d = [], []
for i in range(n):
    arr = list(map(int, input().split()))
    s.append(arr[0])
    d.append(arr[1])

if t in s:
    idx = s.index(t)
    print (idx+1)
else:
    time = []
    count = 0
    for k in range(n):
        tmp = math.ceil((t-s[k])/d[k])
        if tmp >= 0:
            time.append(s[k] + tmp*d[k] - t)
        else:
            time.append(s[k]-t)
            count += 1
    idx = time.index(min(time))
    print (idx+1)
