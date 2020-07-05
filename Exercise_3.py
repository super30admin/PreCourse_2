class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=None
    
class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        node=ListNode(data,None)
        if self.head==None:
            self.head=node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node
        return "node inserted"
    
    def mid(self):
        slow=self.head
        fast= self.head

        while(fast != None):
            
            if fast.next==None or fast.next.next==None:
                break
            slow=slow.next
            fast= fast.next.next
        
        return slow.data



singly=SinglyLinkedList()

print(singly.append(1))
print(singly.append(2))
print(singly.append(3))
# print(singly.append(4))
# print(singly.append(5))
# print(singly.append(6))
# print(singly.append(7))

print(singly.mid())
