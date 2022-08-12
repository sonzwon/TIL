class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, bucketsize=1024):
        self.buckets = [[]]*bucketsize
        self.size = 0
        self.bucketsize = bucketsize
        
    def put(self, key, value):
        idx = hash(key) % self.bucketsize
        for element in self.buckets[idx]:  ##key는 고유한 값이여야하기 떄문에
            if element.key == key:
                element.value == value
                return
        node = Node(key, val)
        self.buckets[idx].append(node)
        self.size+=1