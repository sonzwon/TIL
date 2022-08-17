# [ Binary Search ]
def BinarySearch(arr, target):
    l = 0
    r = len(arr)-1  
    while l<=r:
        m = l + ((r-l)//2)
        if arr[m] < target:
            l = m+1
        elif arr[m] > target:
            r = m-1
        else:
            return m
    return -1

# [ Binary Search Test ]
if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    print(BinarySearch(arr,3)) #2
    print(BinarySearch(arr,7)) #6



# [ Bubble Sort ]
def BubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# [ Bubble Sort Test]               
if __name__ == '__main__':
    arr = [9,1,6,3,7,2,8,4,5,0]
    BubbleSort(arr)
    print(arr)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




# [ Insertion Sort ]
def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and  arr[j]>key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

# [ Insertion Sort Test ]
if __name__ == '__main__':
    arr = [9,1,6,3,7,2,8,4,5,0]
    InsertionSort(arr)
    print(arr)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]