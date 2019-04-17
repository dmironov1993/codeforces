# https://codeforces.com/contest/349/problem/A

n=int(input())
a=list(map(int,input().split()))

state_25 = 0
state_50 = 0
state_100 = 0
res = 'YES'
if a[0] != 25:
    res = 'NO'
else:
    for i in range(n):
        if a[i] == 25:
            state_25 += 1
        elif a[i] == 50:
            state_50 += 1
        else:
            state_100 += 1
        change = a[i] - 25
        while change != 0:
            if change == 75:
                if state_50 != 0:
                    state_50 -= 1
                    change -= 50
                else:
                    state_25 -= 1
                    change -= 25
            else:
                state_25 -= 1
                change -= 25
        if state_25 <0:
            res = 'NO'
            break
print (res)
