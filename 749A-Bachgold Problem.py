# https://codeforces.com/problemset/problem/749/A


n = int(input())

div = n // 2
mod = n % 2
if mod == 0:
    ans = [2]*div
else:
    a = n - 2*(div-1)
    ans = [2]*(div-1) + [a]
print (len(ans))
print (*ans)
