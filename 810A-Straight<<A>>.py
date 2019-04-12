# https://codeforces.com/contest/810/problem/A
# https://codeforces.com/contest/810/submission/52607164

n, k = tuple(map(int, input().split()))
a = list(map(int, input().split()))
add = round(2*((k-0.5)*n - sum(a)) + 0.1)
if add <= 0:
    print (0)
else:
    print (add)
