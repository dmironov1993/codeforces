# https://codeforces.com/contest/1077/submission/52602117

t = int(input()) # number of queries
a = [] # left
b = [] # right
k = [] # number of jumps
for _ in range(t):
    arr = list(map(int, input().split()))
    a.append(arr[0])
    b.append(arr[1])
    k.append(arr[2])
    
def location(a,b,k):
    loc,i = 0,0
    while True: 
        if i == len(k):
            break
        idx = k[i]
        mult = idx // 2
        if idx % 2 == 0:
            loc += (a[i]- b[i])*mult
        else:
            loc += -b[i]*mult + a[i]*(idx - mult)
        i += 1
    return loc
    
for j in range(len(k)):
    ans = location([a[j]],[b[j]], [k[j]])
    print (ans)
