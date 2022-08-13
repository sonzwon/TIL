class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, bucketsize=1024):
        self.buckets = [[]] * bucketsize
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
        
    def get(self, key):
        idx = hash(key)% self.bucketsize
        for element in self.buckets[idx]:
            if element.key == key:
                return element.value
        return None
    
    def delete(self, key):
        idx = hash(key)% self.bucketsize
        for idx, element in enumerate(self.buckets[idx]):
            if element.key == key:
                self.buckets[idx].remove(element)
                self.size -= 1
    
    def contains(self, key):
        idx = hash(key)% self.bucketsize
        for element in self.buckets[idx]:
            if element.key == key:
                return True
        return False
        
    def size(self):
        return self.size