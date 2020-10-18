# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data=data
        self.next=None
        
class LinkedList: 

  #function to initialize the linked list
    def __init__(self): 
        self.head=None
        
  
    # inserting the data to the linked list
    def push(self, new_data): 
        temp=Node(new_data)
        temp.next=self.head
        self.head=temp
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        # applying the two pointers approach to the linked list
        slow_pointer=self.head
        fast_pointer=self.head
        if self.head is not None:
            while (fast_pointer is not None and fast_pointer.next is not None):
                fast_pointer=fast_pointer.next.next
                slow_pointer=slow_pointer.next
            print("The middle element is :", slow_pointer.data)
                

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
