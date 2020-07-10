# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        node = Node(None)
        self.head = node
  
    def push(self, new_data):
        if self.head == None:
            self.head = Node(new_data)
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next =  Node(new_data)
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        print(slow_ptr.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
