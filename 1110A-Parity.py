# https://codeforces.com/contest/1110/problem/A

b, k = tuple(map(int, input().split()))
a = list(map(int, input().split()))
if b % 2 ==0 :
    if a[-1] % 2 == 0:
        print ('even')
    else:
        print ('odd')
else:
    odd = 0
    for i in range(len(a)):
        if a[i] % 2 != 0:
            odd += 1
    if odd % 2 == 0:
        print ('even')
    else:
        print ('odd')
