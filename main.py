n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
for i in range(n):
    print(arr[i])
    print(None)