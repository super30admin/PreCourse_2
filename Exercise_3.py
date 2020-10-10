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
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to get the middle of
    # the linked list
    def printMiddle(self):
        double = self.head
        single = self.head
        while double is not None and double.next is not None:
            double = double.next.next
            single = single.next
        return single.data

    def print_1(self):
        l = self.head
        while l:
            print(l.data)
            l = l.next


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
list1.print_1()
print(list1.printMiddle())
