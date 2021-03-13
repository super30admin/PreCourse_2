# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        # first pointer to jump to element leaving one immediately after it
        # since second pointer reaches exactly the mid when first reaches the end return second pointers data
        twostep_ptr = self.head 
        second_ptr = self.head
        
        if self.head:
            while(first_ptr and first_ptr.next):
                first_ptr = first_ptr.next.next
                second_ptr = second_ptr.next
            return second_ptr.data
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(6)
list1.push(7)
list1.printMiddle() 
