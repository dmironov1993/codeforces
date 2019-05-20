#https://codeforces.com/problemset/problem/1154/A?locale=en

x1,x2,x3,x4 = sorted(list(map(int, input().split())))
a = x4 - x3
b = x4 - x2
c = x4 - x1
print (a,b,c)
