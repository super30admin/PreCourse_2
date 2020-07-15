#Time Complexity : O(n)
#Space Complexity : O(1)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : No

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
      self.data = data
      self.next = None
        
class LinkedList: 
    head = None
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
      slow = self.head
      fast = self.head

      while fast.next is not None and fast.next.next is not None:
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
list1.printMiddle() 
