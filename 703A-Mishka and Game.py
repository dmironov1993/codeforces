# https://codeforces.com/problemset/problem/703/A?locale=ru

n = int(input())

count_m, count_k = 0,0
for i in range(n):
    m, k = tuple(map(int, input().split()))
    if m > k:
        count_m += 1
    elif k > m:
        count_k += 1
if count_m == count_k:
    print ("Friendship is magic!^^")
elif count_m > count_k:
    print ('Mishka')
else:
    print ('Chris')
