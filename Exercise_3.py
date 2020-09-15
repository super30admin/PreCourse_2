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
        node1 = Node(new_data)
        node1.next = self.head
        self.head = node1
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
      slow = self.head
      fast = self.head

      if self.head is not None:
        while fast is not None and fast.next is not None:
          slow = slow.next
          fast = fast.next.next
        print(slow.data)
        

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
