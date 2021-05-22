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
        if self.head == None:
            self.head = Node(new_data)
        else:
            new_Node = Node(new_data)
            new_Node.next = self.head
            self.head = new_Node

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        p1 = self.head
        p2 = self.head
        counter=0
        while p2 !=  None:
            if counter%2 != 0:
                print(p1.next.data)
                p1 = p1.next
            counter = counter+1
            p2 = p2.next
        if p1 != None:
            print("The middle element of the linked list is ",p1.data)




            


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 


""" As we iterate through the whole linkedlist using one pointer,
 and get middle element using the other pointer 
it performs the task in O(n) complexity.
"""