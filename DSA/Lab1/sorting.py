def selectionSort(arr):
    for i in range(len(arr)-1,-1,-1):
        mx=max(arr[0:i+1])
        j=arr.index(mx)
        temp= arr[i]
        arr[i]=arr[j]
        arr[j]=temp
    return arr

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


n = int(input("Enter size of array: "))

arr= []
for i in range(n):
    arr.append(int(input()))

sort=bubbleSort(arr)
print("Sorted list:",sort)