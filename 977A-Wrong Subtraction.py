# https://codeforces.com/problemset/problem/977/A
# https://codeforces.com/contest/977/submission/52775233

n, k = tuple(map(int, input().split()))

for i in range(k):
    if n % 10 == 0:
        n = n // 10
    else:
        n -= 1
print (n)
