
# [[ Array List ]]

class ArrayList:
    def __init__(self, default_size = 5):
        self.size = 0    #데이터 갯수(인덱스가 됨)
        self.max_size = default_size
        self.list = [None] * self.max_size
    
    #배열이 꽉 찼을 때, 배열을 2배로 늘려주는 함수
    def _increase_size(self):
        new_max_size = self.max_size * 2
        new_list = [None] * new_max_size
        for i in range(new_max_size):
            new_list[i] = self.list[i]
        self.max_size = new_max_size
        self.list = new_list

    #배열에 데이터를 입력하는 함수
    def add(self, value):
        if self.size >= self.max_size:
            self._increase_size()   
        self.list[self.size] = value
        self.size += 1

    #인덱스를 지정해 데이터 삽입해주는 함수
    def insert(self, idx, value):
        if self.size >= self.max_size:
            self._increase_size()   
        for i in range(idx, self.size+1):
            self.list[i+1] == self.list[i] #넣고자 하는 인덱스 이후부터 한칸씩 뒤로 미뤄줌
        self.list[idx] = value
        self.size += 1  

    #인덱스를 지정해 데이터 삭제해주는 함수
    def deletebyidx(self, idx):  
        if idx < 0 or idx > self.size:
            raise Exception ("Invalid Index")
        for i in range(idx, self.size):
            self.list[i] = self.list[i+1]  #빼고자 하는 인덱스 이후부터 한칸씩 앞으로 땡겨옴
        self.size -= 1
    
    #해당 데이터를 삭제해주는 함수
    def delete(self, value):
        for i in range(self.size):
            if self.list[i] == value:
                for j in range(i,self.size):
                    self.list[j] == self.list[j+1]
                self.size -= 1
            else:
                raise Exception ("Can not find the data")

    #인덱스로 해당데이터를 읽어오는 함수
    def get(self, idx):
        if idx < 0 or idx > self.size:
            raise Exception ("Invalid Index")
        return self.list[idx]

    #배열에 해당데이터가 포함되어있는지 확인해주는 함수
    def contains(self, value):
        for i in range(self.size+1):
            if self.list[i] == value:
                return True
            else:
                raise Exception ("No data")
    
    #찾고자하는 데이터의 인덱스 리턴해주는 함수
    def indexof(self, value):
        for i in range(self.size+1):
            if self.list[i] == value:
                return i
            else:
                raise Exception ("no data")

    #배열의 사이즈를 리턴해주는 함수
    def size(self):
        return self.size

    #배열이 비었는지 확인해서 리턴해주는 함수
    def isempty(self):
        if self.size == 0:
            return True
        else:
            raise Exception ("Not empty")

    #배열 전체 삭제해주는 함수
    def clear(self):
        self.size = 0
        self.list = []
        
    def getall(self):
        return self.list



# [[ Linked List ]]

# 노드 생성 클래스
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    
    # 노드의 데이터값 리턴해주는 함수    
    def get_data(self):
        return self.data
    
    # 노드의 다음 노드를 리턴해주는 함수
    def get_next(self):
        return self.next_node

    # 노드의 다음 노드를 지정해주는 함수(포인터)
    def set_next(self, new_next):
        self.next_node = new_next
        


class LinkedList(Node):
    def __init__(self, head=None):
         #dummy head node: head가 존재는 하지만, 아무데이터가 없는 상태
        self.head = head    
        self.size = 0
    
    # 리스트 맨 뒤에 데이터 추가해주는 함수
    def add(self, data):
        curr = self.head
        while curr.get_next != None:
            curr = curr.get_next    # 리스트 맨뒤로 이동하게 하는 while문
        new_node = Node(data)       # 추가하고싶은 새로운 노드 생성
        curr.set_next(new_node)     # curr 노드의 다음 노드를 새로 생성한 노드로 포인터
        self.size += 1
        
    def insert(self, idx, data):
        if idx < 0 or idx > self.size:
            raise Exception("Invalid Index")
        i = 0
        prev = self.head       #insert의 경우 포인터를 이동해주는 작업응 해야하므로 prev 노드 설정
        curr = prev.get_next   
        i += 1
        while i < idx:
            prev = prev.get_next
            curr = curr.get_next    #인덱스까지 노드를 이동하게 하는 while문
        new_node = Node(data)       #노드 생성
        prev.set_next(new_node)     #prev노드 다음 노드로 new_node설정
        new_node.set_next(curr)     #new_node 다음 노드로 curr설정 (이렇게 포인터를 바꿔줌으로써 데이터 삽입가능)
        self.size += 1
        
    def clear(self):
        self.size = 0
        return self.head.set_next(None)
    
    def delete(self, data):
        prev = self.head
        curr = prev.get_next
        while curr != None:
            if curr.get_data == data:
                prev.set_next(curr.get_next)
                curr.set_next(None)
                self.size -= 1
            prev = prev.get_next
            curr = curr.get_next
            
    def deletebyindex(self, idx):
        if idx < 0 or idx >= self.size:
            raise Exception("Invalid Index")
        i = 0
        prev = self.head
        curr = prev.get_next
        i += 1
        while i < idx:
            prev = prev.get_next
            curr = curr.get_next
        prev.set_next(curr.get_next)
        curr.set_next(None)
        self.size -= 1
        return True
    
    def get(self, idx):
        if idx < 0 or idx >= self.size:
            raise Exception("Invalid Index")
        curr = self.head.get_next  #dummy node이기 때문에(head에 데이터가 없음)
        i = 0
        i += 1
        while i < idx:
            curr = curr.get_next
        return curr.get_data
    
    def indexof(self, data):
        curr = self.head.get_next
        idx = 0
        while curr != None:
            if curr.get_data == data:
                return idx
            curr = curr.get_next
            idx += 1
        return -1
    
    def isEmpty(self):
        if self.head.get_next == None:
            return True
        
    def contains(self, data):
        curr = self.head.get_next
        while curr != None:
            if curr.get_data == data:
                return True
            curr = curr.get_next
    
    def size(self):
        return self.size