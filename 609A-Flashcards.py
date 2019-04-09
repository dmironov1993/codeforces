# https://codeforces.com/contest/609/problem/A

n = int(input())
m = int(input())
a = [int(input()) for _ in range(n)]

def BubbleSort(n, a):
    for passnum in range(n-1, 0, -1):
        for i in range(passnum):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                
BubbleSort(n, a)
summa = 0
count = 0
for i in range(1,n+1):
    if summa < m:
        summa += a[-i]
        count += 1
    elif summa >= m:
        break
print (count)
