# https://codeforces.com/problemset/problem/996/A


n = int(input())
a = [100,20,10,5,1]
k = len(a)
count = 0
for i in range(k):
    b = n // a[i]
    if b > 0:
        count += n // a[i]
        n = n % a[i]
print (count)
