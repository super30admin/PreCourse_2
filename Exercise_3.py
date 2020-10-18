# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

#Traverses the entire list and prints each item
    def printList(self):
        curr = self.head
        if curr is None:
            print("The list is empty. ")
        else:
            print("The items in the list are : ")
            while curr is not None:
                print(curr.data)
                curr = curr.next

#Traverses the entire list and pushes the new item at the end of th list1
#Time Complexity = O(n) Space Complexity=O(1)
    def push(self, new_data):
        n = Node(new_data)
        if self.head == None:
            self.head = n
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = n

#There are two pointers , ptr1 moves one node at a time whereas ptr2 jumps 2 nodes.
#ptr1 points to the middle element of the list whereas ptr1 keeps track of the end of the list1
#Time Complexity=O(n) Space Complexity = O(1)

    def printMiddle(self):
        ptr1 = self.head
        ptr2 = self.head

        while(ptr2.next is not None and ptr2.next.next is not None):
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next

        print("Middle element of the linked list is : {}".format(ptr1.data) )

# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.printMiddle()
