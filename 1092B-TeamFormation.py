# https://codeforces.com/contest/1092/problem/B

n = int(input())
arr = list(map(int, input().split()))

def insertionSort(n, arr):
    for index in range(n):
        currentvalue = arr[index]
        position = index
        while position > 0 and arr[position-1] > currentvalue:
            arr[position] = arr[position-1]
            position = position - 1
            arr[position] = currentvalue

def counting(n, arr):
    if n == 2:
        return abs(arr[0] - arr[1])
    else:
        insertionSort(n, arr)
        new_list = []
        for i in range(1,n,2):
            new_list.append(abs(arr[i] - arr[i-1]))
        return sum(new_list)

ans = counting(n,arr)
print (ans)
