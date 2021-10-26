class Node:
    """Node class, has next, prev, and data"""

    def __init__(self, data, next, prev):
        self.data_ = data
        self.next_ = next
        self.prev_ = prev


    def get_data(self):
        return self.data_

    def get_next(self):
        return self.next_

    def get_prev(self):
        return self.prev_

    def set_data(self, data):
        self.data_ = data

    def set_next(self, next):
        self.next_ = next
    
    def set_prev(self, prev):
        self.prev_ = prev