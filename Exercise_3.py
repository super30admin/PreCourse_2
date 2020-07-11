# Node class
class Node:
    data = None
    nxt = None
    prev = None
    
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.nxt = None
        self.prev = None


class LinkedList:
    size = 0
    middle = None
    head = None
    tail = None
    
    def __init__(self):
        self.middle = None
        self.head = Node('*')
        self.tail = Node('*')
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.nxt = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.nxt = new_node
        self.tail.prev = new_node
        self.size += 1
        if not self.middle:
            self.middle = new_node
        elif self.size % 2 == 0:
            self.middle = self.middle.nxt
        return
        
        # Function to get the middle of
    
    # the linked list
    def printMiddle(self):
        if self.middle:
            print self.middle.data

    def printList(self):
        current = self.head.nxt
        while current.nxt:
            print(current.data)
            current = current.nxt

# Driver code 
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()
