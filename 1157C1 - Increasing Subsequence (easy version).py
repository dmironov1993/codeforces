# https://codeforces.com/contest/1157/problem/C1


n = int(input())
a = list(map(int, input().split()))
res = []
num = []
l = a[0]
r = a[-1]
if l < r:
    num.append(l)
    res.append('L')
    a.pop(0)
else:
    num.append(r)
    res.append('R')
    a.pop(-1)

if n == 1:
    print (1)
    print (res[0])
elif n == 2:
    if a[0] > num[-1]:
        res.append('R')
    print (len(res))   
    print (''.join(res))
else:    
    i, j, k = 0, 0, 0
    while True:
        l = a[i]
        r = a[-j-1]
        if (r > num[-1] and r <= l) or (r > num[-1] and l <= num[-1]):
            res.append('R')
            num.append(r)
            j += 1
        elif (l > num[-1] and l < r) or (l > num[-1] and r < num[-1]):
            res.append('L')
            num.append(l)
            i += 1
        else:
            break
        if i + j == n-1:
            break
    print (len(res))
    print (''.join(res))
