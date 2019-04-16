# https://codeforces.com/contest/141/problem/A

guest = input()
host = input()
letters = input()

def searching(s1,s2,col):
    possible = True
    s = s1 + s2
    if len(s) != len(col):
        possible = False
    else:
        collist = list(col)
        idx = 0
        while idx < len(s) and possible:
            if s[idx] in collist:
                loc = collist.index(s[idx])
                collist[loc] = None
            else:
                possible = False
            idx = idx + 1
    
    if possible:
        return 'YES'
    else:
        return 'NO'
        
ans = searching(guest,host,letters)
print (ans)
