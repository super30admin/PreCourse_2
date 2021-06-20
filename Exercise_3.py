# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        
  
    def push(self, new_data): # O(n)
        new_node = Node(new_data)
        
        if self.head is None:                
            self.head = new_node
            return
        
        last_node = self.head              
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def length(self, head): # O(n)
        curr_node = head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count
    
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        leng = self.length(self.head)
        
        pos = leng//2
        
        count = 0
        curr_node = self.head
        while curr_node and count != pos:
            curr_node = curr_node.next
            count += 1
        print(curr_node.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

