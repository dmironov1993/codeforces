# https://codeforces.com/contest/1093/problem/B

t = int(input())
s = [input() for _ in range(t)]
d = [x[-1::-1] for x in s]
for i in range(t):
    if s[i] == d[i]:
        s1 = sorted(s[i])
        s2 = sorted(d[i])
        s2[0], s2[-1] = s2[-1], s2[0]
        if s2[0] == s1[0]:
            print (-1)
        else:
            print (''.join(s2))
    else:
        print (d[i])
