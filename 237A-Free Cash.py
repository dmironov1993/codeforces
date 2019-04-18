# https://codeforces.com/contest/237/problem/A


n=int(input())
time = []
time_z = []
for _ in range(n):
    arr = input().split()
    if arr[0] == '0':
        time_z.append(arr[1])
    else:
        if int(arr[1]) < 10:
            arr[1] = '0' + arr[1]
        time.append(arr[0] + arr[1])
times = list(map(int,time))
time_z = list(map(int, time_z))

def search(nums):
    d = {}
    count = 0
    for el in nums:
        d[el] = d[el] + 1 if el in d.keys() else 1
        if d[el] > count:
            count = d[el]
    return count
        
    
res = search(times)
res_z = search(time_z)
if res > res_z:
    print (res)
else:
    print (res_z)
