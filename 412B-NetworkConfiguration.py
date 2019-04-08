# https://codeforces.com/problemset/problem/412/B

arr = list(map(int, input().split()))
n, k = arr[0], arr[1]

a = sorted(list(map(int, input().split())), reverse=True)
print (a[k-1])
