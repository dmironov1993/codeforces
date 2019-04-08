# https://codeforces.com/problemset/problem/984/A

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
            
def game(n, arr):
    if n == 1:
        return arr[0]
    else:
        insertionSort(n, arr)
        stop = False
        while not stop:
            arr.pop(-1)
            if len(arr) == 1:
                break
            arr.pop(0)
            if len(arr) == 1:
                break
        return arr[0]
        
ans = game(n, arr)
print (ans)
