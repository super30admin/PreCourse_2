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
        if self.head is None:
            self.head = Node(new_data)
        else:
            self.currentNode = self.head
            while self.currentNode.next is not None:
                self.currentNode = self.currentNode.next
            self.currentNode.next = Node(new_data)        
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        self.slow = self.head
        self.fast = self.head
        # Both fast as well as slow pointers start from the head position
        # Fast pointer moves by 2 steps while slow pointer moves by one step
        # By the time, fast pointer reaches the end of the LinkedList, fast pointer is at twice the distance of slow pointer, hence, slow pointer sits at the middle node
        # Return the value of the node which the slow pointer is pointing to. 
        # Time complexity is O(n)
        while self.fast.next is not None:
            self.fast = self.fast.next.next
            self.slow = self.slow.next
        return self.slow.data    

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(1) 
list1.push(3) 
print(list1.printMiddle())
