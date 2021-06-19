# Time Complexity : O(n)
# Space Complexity : O(1)

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
        node_new = Node(new_data)
        node_new.next = self.head
        self.head = node_new
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        pointer1 = self.head
        pointer2 = self.head
        if self.head is not None:
            while(pointer2 is not None and pointer2.next is not None):
                pointer2 = pointer2.next.next
                pointer1 = pointer1.next
            print("The middle element is ", pointer1.data) 

# Driver code 
list1 = LinkedList() 
list1.push(6)
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
