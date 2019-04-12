# https://codeforces.com/contest/263/problem/B
# https://codeforces.com/contest/263/submission/52577964


n,k = tuple(map(int, input().split()))
a = sorted(list(map(int, input().split())))

if k < len(a):
    if a[-k] - a[-k-1] > 1:
        print (*[a[-k]-1,0])
    elif a[-k] - a[-k-1] == 1:
        print (*[a[-k],0])
    else:
        print (-1)
elif k == len(a):
    print (*[a[-k]-1,0])
else:
    print (-1)
