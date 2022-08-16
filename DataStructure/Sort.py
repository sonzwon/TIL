# [ BinarySearch ]
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

#[ Test ]
if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    print(BinarySearch(arr,3)) #2
    print(BinarySearch(arr,7)) #6