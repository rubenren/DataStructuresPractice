from node import Node

class LinkedList:
    """A linked list to hold nodes"""
    # Apparently linked lists using pointers are not that great for speed
    # because they tend to not have any particular pattern when stored in memory,
    # which causes a higher chache miss count than an array which is contiguous in memory

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
        """Remove the front element and return it"""

        if self.size_ == 0:
            raise Exception('Can\'t pop from an empty list!')
        if self.size_ == 1:
            retVal = self.head_.get_data()
            self.head_ = None
            self.tail_ = None
            return retVal

        retVal = self.head_.get_data()

        self.head_ = self.head_.get_next()
        
        self.head_.set_prev(None)

        self.size_ -= 1

        return retVal

    def push_back(self, data):
        self.insert(self.size_, data)

    def pop_back(self):
        """Removes the back element and returns it's value"""

        if self.size_ == 0:
            raise Exception('Can\'t pop from an empty list!')
        if self.size_ == 1:
            retVal = self.head_.get_data()
            self.head_ = None
            self.tail_ = None
            return retVal

        retVal = self.tail_.get_data()

        self.tail_ = self.tail_.get_prev()

        self.tail_.set_next(None)

        self.size_ -= 1

        return retVal

    def front(self):
        """Returns the value of the front element"""
        return self.head_.get_data()

    def back(self):
        """Returns the value of the back element"""
        return self.tail_.get_data()

    def __find_node(self, idx):
        """Private mehtod to get the node object of an index"""
        # Can be improved to save a bit of time
        if self.size_ != 0: idx = idx % self.size_
        else: idx = 0
        
        retNode = self.head_
        for i in range(idx):
            retNode = retNode.get_next()
        
        return retNode

    def insert(self, idx, data):
        """Places a new node with the data in the index specified"""
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
        """Erases the given index value"""
        toBeGone = self.__find_node(idx)

        if toBeGone.get_next():
            toBeGone.get_next().set_prev(toBeGone.get_prev())
        if toBeGone.get_prev():
            toBeGone.get_prev().set_next(toBeGone.get_next())

        del toBeGone

        self.size_ -= 1

    def value_n_from_end(self, n):
        """Returns the value fron the node n away from the end"""
        return self.__find_node(self.size_ - n - 1).get_data()

    def reverse(self):
        """Reverses the order of the list"""

        temp = None
        curr = self.head_
        while curr.get_next() != None:
            temp = curr.get_prev()
            curr.set_prev(curr.get_next())
            curr.set_next(temp)
            curr = curr.get_prev() # Really bad for readability should improve later

        temp = self.tail_
        self.tail_ = self.head_
        self.head_ = temp

    def __delete_node(self, inNode):
        if inNode.get_prev():
            temp = inNode.get_prev()
        if inNode.get_next():
            temp.set_next(inNode.get_next())
        del inNode
        

    def remove_value(self, target):
        """Remove the first instance of the value"""
        temp = self.head_
        for i in range(self.size_):
            if temp.get_data() == target:
                self.__delete_node(temp)
                self.size_ -= 1
                return
            temp = temp.get_next()
