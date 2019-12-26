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
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node
  
    # Function to get the middle of  
    # the linked list
    # using 2 pointer approach
    def printMiddle(self):
        fast_ptr = self.head
        slow_ptr = self.head
        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next

        print("The middle element in the linked list is: ", slow_ptr.data)
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
