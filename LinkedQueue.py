import Node

class LinkedQueue:

    def __init__(self): # initialize
        self.top = None
        self.rear = None
        self.length = 0

    def __str__(self): # string output of Queue object
        s = "" # start with empty string
        next = self.top
        while next != None: # go through the linked list
            s += str(next.get_data())
            s += " "
            next = next.get_next()
        return(s)

    def is_empty(self): # boolean, true if empty, false if not empty
        return self.top == None

    def enqueue(self, item): # add item to the end of the queue
        node = Node.Node(item)
        if self.is_empty(): # if the Queue is empty make the node the top and the rear
            self.top = node
            self.rear = node
            self.length += 1
        else: # if the node is not empty, make the node the rear
            self.rear.set_next(node)
            self.rear = node
            self.length += 1

    def dequeue(self): # removes nand returns the item at the front of the queue
        if self.top == None:
            return(None)
        else:
            top = self.top.get_data()
            self.top = self.top.get_next()
            self.length = self.length - 1
            return(top)

    def first(self): # returns but does not remove the first item
        if self.top == None:
            return(None)
        top = self.top.get_data()
        return(top)

    def size(self): # size of Queue
        return self.length

