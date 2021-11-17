import Node
import LinkedQueue

class LinkedDeque(LinkedQueue.LinkedQueue):

    def __init__(self): # initialize
        super().__init__()

    def __str__(self): # string value of the Deque
        return(super().__str__())

    def add_front(self, item): # adds item to the front of the Deque
        node = Node.Node(item)
        if self.is_empty():
            self.top = node
            self.rear = node
            self.length += 1
        else:
            prevTop = self.top
            self.top = node
            self.top.set_next(prevTop)
            self.length += 1

    def add_rear(self, item): # adds item to the end of the deque
        super().enqueue(item)

    def remove_front(self): # removes and returns the front
        return(super().dequeue())

    def remove_rear(self): # removes and returns the rear
        checknode = self.top
        previousNode = checknode
        if checknode.get_next() == None:
            self.rear = None
            self.top = None
            self.length = self.length - 1
        else:
            while(checknode.get_next() is not None):
                previousNode = checknode
                checknode = checknode.get_next()
            self.length = self.length - 1
            self.rear = previousNode
            previousNode.set_next(None)
        return checknode.get_data()

    def get_front(self): # returns but does not remove the front
        return(super().first())

    def get_rear(self): # returns but does not remove the rear
        return(self.rear.get_data())

    def size(self): # returns the size of the Deque object
        return(super().size())

    def is_empty(self): # check to see if Deque object is empty
        return(super().is_empty())
