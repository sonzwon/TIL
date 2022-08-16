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
    for i in range(len(arr)-1): #전체리스트 순환
        for j in range(len(arr)-1-i): #정렬된 element제외하고 순환
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# [ Bubble Sort Test]               
if __name__ == '__main__':
    arr = [9,1,6,3,7,2,8,4,5,0]
    BubbleSort(arr)
    print(arr)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]