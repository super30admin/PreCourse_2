# Node class  

## Time Complexity = O(1) for insertion, O(n) for  getting the middle element
## Space Complexity  =  O(N) to store the linked list . No auxillary space is used

class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.val = data
        self.next = None
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.start = None
  
    def push(self, new_data): 
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            self.start = new_node
            return
        self.head.next = new_node
        self.head = new_node
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.start
        if not slow:
            print(None)
            return
        fast = slow.next
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        print(slow.val)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
