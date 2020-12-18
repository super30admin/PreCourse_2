# Node class  
class Node:  
    #Create node in a LL
    # Function to initialise the node object  
    def __init__(self, data, next=None):  
        self.data = data 
        self.next = next 

class LinkedList: 
    #O(1) creates new LinkedList
    def __init__(self): 
        self.head = None 

    #O(n) inserts new element at end of LL
    def push(self, new_data): 
        newNode = Node(new_data)
        #if nothing in LL
        if not self.head:
            self.head = newNode
            return 
        curr = self.head 
        while curr.next:
            curr = curr.next 
        curr.next = newNode
  
    # Function to get the middle of  
    # the linked list 
    #time: O(N/2) -> O(N)
    def printMiddle(self): 
        slow = self.head 
        fast = self.head 
        #since fast is moving twice as fast, when we reach the end, the slow pointer will be the middle 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        print(slow.data)
        return  
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
# 5 4 2 3 1 should return 2