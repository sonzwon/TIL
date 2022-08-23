# [ Min Heap ]
class MinHeap:
    def __init__(self, list):
        self.data = list

    def insert(self, value):
        self.data.append(value)
        self.insert_heapify(len(self.data) - 1)
        
    def insert_heapify(self, idx):
        parent = (idx - 1) // 2
        if parent >= 0:
            if self.data[idx] < self.data[parent]:
                self.data[idx] =  self.data[parent]
                self.data[parent] = self.data[idx]
                self.insert_heapify(parent)

    def pop(self):
        top = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.pop_heapify(0)
        return top

    def pop_heapify(self, idx):
        if self.isLeaf(idx):
            return
        left = 2 * idx + 1
        right = 2 * idx + 2
        curr = idx

        if left < len(self.data) and self.data[left] < self.data[curr]:
            curr = left
        if right < len(self.data) and self.data[right] < self.data[curr]:
            curr = right
        if curr != idx:
            self.data[idx], self.data[curr] = self.data[curr], self.data[idx]
            self.pop_heapify(curr)

    def isLeaf(self, pos):
        if pos > len(self.data)//2 and pos <= len(self.data):
            return True
        
    def contains(self, value):
        for i in range(len(self.data)):
            if value == self.data[i]:
                return True
            return False

    def peek(self):
        if len(self.data) < 1:
            raise Exception()
        return self.data[0]

    def size(self):
        return len(self.data)


# [ Min Heap Test ]
if __name__ == "__main__":
    min_heap = MinHeap([2,6,3,7,8,5])
    print(f"min_heap.insert(1)")
    min_heap.insert(1)
    print(f"min_heap.size(): {min_heap.size()}")
    print(f"min_heap.peek(): {min_heap.peek()}")
    print("===========================================")
    print(f"min_heap.pop(): {min_heap.pop()}")
    print(f"min_heap.size(): {min_heap.size()}")
    print(f"min_heap.peek(): {min_heap.peek()}")






# [ Max Heap ]
class MaxHeap:
    def __init__(self, list):
        self.data = list

    def insert(self, value):
        self.data.append(value)
        self.insert_heapify(len(self.data) - 1)
        
    def insert_heapify(self, idx):
        parent = (idx - 1) // 2
        if parent >= 0:
            if self.data[idx] > self.data[parent]:
                self.data[idx] = self.data[parent]
                self.data[parent] = self.data[idx]
                self.insert_heapify(parent)

    def pop(self):
        top = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.pop_heapify(0)
        return top

    def pop_heapify(self, idx):
        if self.isLeaf(idx):
            return
        left = 2 * idx + 1
        right = 2 * idx + 2
        curr = idx

        if left < len(self.data) and self.data[left] > self.data[curr]:
            curr = left
        if right < len(self.data) and self.data[right] > self.data[curr]:
            curr = right
        if curr != idx:
            self.data[idx], self.data[curr] = self.data[curr], self.data[idx]
            self.pop_heapify(curr)

    def isLeaf(self, pos):
        if pos > len(self.data)//2 and pos <= len(self.data):
            return True
        
    def contains(self, value):
        for i in range(len(self.data)):
            if value == self.data[i]:
                return True
            return False

    def peek(self):
        if len(self.data) < 1:
            raise Exception()
        return self.data[0]

    def size(self):
        return len(self.data)


# [ Max Heap Test ]
if __name__ == "__main__":
    max_heap = MaxHeap([9,5,7,4,2,6])
    print(f"max_heap.insert(10)")
    max_heap.insert(10)
    print(f"max_heap.size(): {max_heap.size()}")
    print(f"max_heap.peek(): {max_heap.peek()}")
    print("===========================================")
    print(f"max_heap.pop(): {max_heap.pop()}")
    print(f"max_heap.size(): {max_heap.size()}")
    print(f"max_heap.peek(): {max_heap.peek()}")