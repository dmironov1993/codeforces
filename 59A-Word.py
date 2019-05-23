# https://codeforces.com/problemset/problem/59/A?locale=ru

s = input()
k = len(s)

l, u = 0,0
for i in range(k):
    if s[i].isupper():
        u += 1
    else:
        l += 1
if u > l:
    print (s.upper())
else:
    print (s.lower())
