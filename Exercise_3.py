# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = Node(0)
  
    def push(self, new_data): 
        node = self.head 
        while node.next is not None:
            node = node.next
        node.next = Node(new_data)    
  
    # Function to get the middle of  
    # the linked list 
    
    # Time: O(log n) | O(1) space, where n are the number of nodes.
    def printMiddle(self): 
        slow = fast = self.head.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next 
        print(slow.data)
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
# list1.push(0) 
list1.printMiddle() 
