# https://codeforces.com/contest/75/problem/A

a = input()
b = input()

a_lhs = []
for i in range(len(list(a))):
    if list(a)[i] != '0':
        a_lhs.append(list(a)[i])
        
b_lhs = []
for j in range(len(list(b))):
    if list(b)[j] != '0':
        b_lhs.append(list(b)[j])
        
lhs = int(''.join(a_lhs)) + int(''.join(b_lhs))

rhs_z = list(str(int(a) + int(b)))
rhs = []
for k in range(len(rhs_z)):
    if rhs_z[k] != '0':
        rhs.append(rhs_z[k])
rhs = int(''.join(rhs))

if lhs == rhs:
    print ('YES')
else:
    print ('NO')
