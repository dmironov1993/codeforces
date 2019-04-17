# https://codeforces.com/contest/710/problem/A

pos = input()
three = ['a8','h8','h1','a1']

if pos in three:
    print (3)
else:
    if pos[1] == '8' or pos[1] == '1' or pos[0] == 'a' or pos[0] == 'h':
        print (5)
    else:
        print (8)
