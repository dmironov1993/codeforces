# https://codeforces.com/contest/432/problem/A

n, k = tuple(map(int, input().split()))
y = list(map(int, input().split()))

y_mod = [i+k for i in y if i+k <= 5]
print (len(y_mod)//3)
