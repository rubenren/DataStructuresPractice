from node import Node

class LinkedList:
    """A linked list to hold nodes"""

    def __init__(self):
        self.head_ = None
        self.tail_ = None
        self.size_ = 0

    def size(self):
        return self.size_

    def is_empty(self):
        return self.size_ == 0

    def value_at(self, idx_in):
        # If the size is zero, throws error
        if self.size_ == 0:
            raise Exception('Can\'t reference from an empty list!')

        # Wrap the idx by the size
        idx = idx_in % self.size_

        tempNode = self.head_
        for i in range(idx):
            tempNode = tempNode.get_next()
        
        return tempNode.get_data()
    
    def push_front(self, data):
        self.insert(0, data)

    def pop_front(self):
        pass

    def push_back(self, data):
        self.insert(self.size_, data)

    def pop_back(self):
        pass

    def front(self):
        pass

    def back(self):
        pass

    def __find_node(self, idx):
        if self.size_ != 0: idx = idx % self.size_
        else: idx = 0
        
        retNode = self.head_
        for i in range(idx):
            retNode = retNode.get_next()
        
        return retNode

    def insert(self, idx, data):
        if self.size_ != 0: idx = idx % (self.size_ + 1)
        else: idx = 0

        newNode = Node(data, None, None)

        if self.size_ == 0:
            self.head_ = newNode
            self.tail_ = newNode
        elif idx == 0:
            newNode.set_next(self.head_)
            self.head_.set_prev(newNode)
            self.head_ = newNode
        elif idx == self.size_:
            newNode.set_prev(self.tail_)
            self.tail_.set_next(newNode)
            self.tail_ = newNode
        else:
            tempNode = self.__find_node(idx)
            newNode.set_next(tempNode)
            newNode.set_prev(tempNode.get_prev())
            newNode.get_next().set_prev(newNode)
            newNode.get_prev().set_next(newNode)

        self.size_ += 1


    def erase(self, idx):
        pass

    def value_n_from_end(self, n):
        pass

    def reverse(self):
        pass

    def remove_value(self, target):
        pass
