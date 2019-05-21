# https://codeforces.com/problemset/problem/509/A?locale=ru

n = int(input())
a = [1]*n

def recursion(i,j):
    if j == 1:
        return 1
    if i == 1:
        return 1
    return recursion(i-1,j) + recursion(i,j-1)

print (recursion(n,n))
