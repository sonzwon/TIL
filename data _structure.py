class ArrayList:
    def __init__(self, default_size = 50):
        self.size = 0    #데이터 갯수(인덱스가 됨)
        self.max_size = default_size
        self.list = [None] * self.max_size
    
    #배열이 꽉 찼을 때, 배열을 2배로 늘려주는 함수
    def _increase_size(self):
        new_max_size = self.max_size * 2
        new_list = [None] * new_max_size
        for i in range(new_max_size):
            new_list[i] = self.list[i]

    #배열에 데이터를 입력하는 함수
    def add(self, value):
        if self.size >= self.max_size:
            self._increase_size   
        self.list[self.size] = value
        self.size += 1

    #인덱스를 지정해 데이터 삽입해주는 함수
    def insert(self, idx, value):
        if self.size == self.max_size:
            self._increase_size   
        for i in range(idx, self.size+1):
            self.list[i+1] == self.list[i] #넣고자 하는 인덱스 이후부터 한칸씩 뒤로 미뤄줌
        self.list[idx] = value
        self.size += 1  

    #인덱스를 지정해 데이터 삭제해주는 함수
    def deletebyidx(self, idx):  
        if idx < 0 or idx > self.size:
            raise Exception ("Invalid Index")
        for i in range(idx, self.size+1):
            self.list[i] = self.list[i+1]  #빼고자 하는 인덱스 이후부터 한칸씩 앞으로 땡겨옴
        self.size -= 1
    
    #해당 데이터를 삭제해주는 함수
    def delete(self, value):
        for i in range(self.size+1):
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

new_array = ArrayList()
new_array.add(5)