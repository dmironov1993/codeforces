# https://codeforces.com/contest/514/problem/A

x = list(map(int,list(input())))
n = len(x)
if 9 - x[0] > 0 and 9-x[0] < x[0]:
    x[0] = 9-x[0]
for i in range(1,n):
    num = 9 - x[i]
    if num < x[i] and num >= 0:
        x[i] = num
x = list(map(str, x))
print(''.join(x))
