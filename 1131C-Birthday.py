# https://codeforces.com/contest/1131/problem/C

n = int(input())
a = sorted(list(map(int, input().split())))
left = [a[i] for i in range(0,n,2)]
right = sorted([a[i] for i in range(1,n,2)],reverse=True)

print (*(left + right))
