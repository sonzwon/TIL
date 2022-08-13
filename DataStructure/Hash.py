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
        node = Node(key, value)
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
    
    
    
## Test
if __name__ == "__main__":
    table = HashTable()
    print("table.put('k1','v1')")
    table.put('k1','v1')
    print("table.put('k2','v2')")
    table.put('k2','v2')
    print("table.put('k3','v3')")
    table.put('k3','v3')
    print("table.get('k1') : {}".format(table.get('k1')))
    print("table.get('k2') : {}".format(table.get('k2')))
    print("table.get('k3') : {}".format(table.get('k3')))
    print("table.put('k2','v4')")
    table.put('k2','v4')
    print("table.get('k2') : {}".format(table.get('k2')))
    print("table.delete('k2')")
    table.delete('k2')
    print("table.get('k1') : {}".format(table.get('k1')))
    print("table.get('k2') : {}".format(table.get('k2')))
    print("table.get('k3') : {}".format(table.get('k3')))


# 해결해야할 오류
# 1) put메서드 key값 충돌일어났을 때, 덮어쓰기 기능 안됨
# 2) table.size 실행시 TypeError: 'int' object is not callable 발생