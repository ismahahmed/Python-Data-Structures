import Node

class LinkedStack:

    def __init__(self): # initialize 
        self.top = None
        self.length = 0

    def __str__(self): # string output of self object
        s = ""
        next = self.top
        while next != None:
            s += str(next)
            s += " " # space in between each item
            next = next.get_next() # get next item
        return(s)

    def push(self,item): # add item to top of stack
        node = Node.Node(item) # create node object
        node.set_next(self.top) 
        self.top = node
        self.length += 1 # add 1 to length

    def pop(self): # removes and returns at top
        if self.is_empty(): # check to see if stack is empty
            return None # return None if stack is empty
        else:
            item = self.top.get_data() # get data from the top stack/first node
            self.top = self.top.get_next() # make the second node the new top
            self.length = self.length-1 # subtract 1 from the stack length 
            return item # return the previous top

    def peek(self): # returns but does not remove the top of the stack
        if self.is_empty(): # if it is empty, return None
            return None
        else: # if it is not empty, get the data of the top stack/first node
            return self.top.get_data()

    def size(self): # returns the number of items in the stack
        return self.length

    def is_empty(self): # Boolean, true if empty, false if not
        return self.top == None

