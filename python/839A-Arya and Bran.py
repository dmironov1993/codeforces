n, k = map(int, input().split())
a = list(map(int, input().split()))

day = 0
num = 0
i = 0
while True:
    if a[i] > 8:
        a[i] -= 8
        num += 8
        if i+1 <= n-1:
            a[i+1] += a[i]
    else:
        num += a[i]
        a[i] = 0
        if i+1 <= n-1:
            a[i+1] += a[i]
    i += 1
    day += 1
    if num >= k or day == n:
        break
    
    

print (day if day > 0 and k <= num else -1)
