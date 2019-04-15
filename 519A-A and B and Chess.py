# https://codeforces.com/problemset/problem/519/A

# white
dct_w = {'Q':9,
       'R':5,
       'B':3,
       'N':3,
       'P':1,
       'K':0}
# black
dct_b = {'q':9,
       'r':5,
       'b':3,
       'n':3,
       'p':1,
       'k':0}
arr = []
for i in range(8):
    name = list(input())
    for k in range(8):
        arr.append(name[k])
    

count_w = 0
count_b = 0
for el in arr:
    if el in dct_w.keys():
        count_w += dct_w[el]
    elif el in dct_b.keys():
        count_b += dct_b[el]
        
if count_w > count_b:
    print ('White')
elif count_w == count_b:
    print ('Draw')
else:
    print('Black')
