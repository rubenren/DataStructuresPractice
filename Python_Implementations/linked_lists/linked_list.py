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

    def at(self, idx_in):
        # If the size is zero, throws error
        if self.size_ == 0:
            raise Excpetion('Can\'t reference from an empty list!')

        # Wrap the idx by the size
        idx = idx_in % self.size_

        tempNode = self.head_
        for i in range(idx):
            tempNode = tempNode.get_next()
        
        return tempNode
    
    def push_front(self, data):
        pass

    def pop_front(self):
        pass

    def push_back(self, data):
        pass

    def pop_back(self):
        pass

    def front(self):
        pass

    def back(self):
        pass

    def insert(self, idx, data):
        pass

    def erase(self, idx):
        pass

    def value_n_from_end(self, n):
        pass

    def reverse(self):
        pass

    def remove_value(self, target):
        pass
