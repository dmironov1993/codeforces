# https://codeforces.com/contest/1132/problem/B

n = int(input()) # number of bars
a = sorted(list(map(int, input().split())), reverse=True)  # cost of a bar
m = int(input())  # number of coupons
q = list(map(int, input().split()))  # 
summa = sum(a)

for el in q:
    print (summa - a[el-1])
