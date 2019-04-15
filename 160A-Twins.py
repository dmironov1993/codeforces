# https://codeforces.com/contest/160/problem/A

n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

count_me = 0
summa = 0
condition_1 = 0
condition_2 = 0
for i in range(n):
    count_me += 1
    summa += a[i]
    if sum(a[i+1:]) < summa:
        break
        
print (count_me)
