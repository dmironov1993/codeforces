# https://codeforces.com/problemset/problem/431/A

a = list(map(int, input().split()))
b = input()


count, n = 0, len(b)
for i in range(n):
    k = int(b[i])
    count += a[k-1]
print (count)
