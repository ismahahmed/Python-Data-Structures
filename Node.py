class Node:

    def  __init__(self,d=None):
        self._data = d
        self._next = None

    def get_data(self):
        return self._data

    def set_data(self, d):
        self._data = d

    def get_next(self):
        return self._next

    def set_next(self, node_next): #takes in an already-instantiated node
        self._next = node_next

    def __str__(self):
        return(str(self._data))
