# https://codeforces.com/contest/753/submission/53101819

n = int(input())

a = []
for i in range(1,n+1):
    if n - i >= 0:
        a.append(i)
        n -= i

for j in range(1,n+1):
    if n - j >= 0:
        a[-j] += 1
print (len(a))
print (*a)
