# https://codeforces.com/contest/653/problem/A

n = int(input())
t = list(map(int, input().split()))

def BubbleSort(n, arr):
    for pannum in range(n-1,0,-1):
        for i in range(pannum):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

def delete_duplicates(n, arr):
    array = arr.copy()
    for i in range(n-1):
        el = arr[i]
        for j in range(i+1,n):
            if el == arr[j]:
                array[j] = 0

    sub_array = []
    for k in range(n):
        if array[k] != 0:
            sub_array.append(array[k])
    return sub_array
    
BubbleSort(n, t)
t = delete_duplicates(n, t)
res = 'No'
if len(t) > 2:
    for k in range(len(t)-2):
        if t[k+2] - t[k] <= 2 and t[k+2] - t[k] > 0 and t[k+1] != t[k] and t[k+2] != t[k+1]:
            res = 'Yes'
            break
print (res)
