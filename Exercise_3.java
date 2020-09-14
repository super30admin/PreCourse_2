class LinkedList 
{ 
    Node head; // head of linked list 
  
    /* Linked list node */
    class Node 
    { 
        int data; 
        Node next; 
        Node(int d) 
        { 
            data = d; 
            next = null; 
        } 
    } 
  
    /* Function to print middle of linked list */
   //Complete this function
    void printMiddle() // this fuciton will run n/2 times 
                       // time complexity O(n) and space complexity O(1)
    { 
        //Write your code here
    //Implement using Fast and slow pointers
    { 
        Node slow = head; 
        Node fast = head; 
        if (head != null) 
        { 
            while (fast != null && fast.next != null) 
            { 
                fast = fast.next.next; 
                slow = slow.next; 
            } 
            System.out.println("The middle element is [" + 
                                slow.data + "] \n"); 
        } 
    }
    } 
  
    public void push(int new_data) 
    { 
        Node new_node = new Node(new_data); 
        new_node.next = head; 
        head = new_node; 
    } 

    public void printList() // time O(n) space O(1)
    { 
        Node tnode = head; 
        while (tnode != null) 
        { 
            System.out.print(tnode.data+"->"); 
            tnode = tnode.next; 
        } 
        System.out.println("NULL"); 
    } 
  
    public static void main(String [] args) 
    { 
        LinkedList llist = new LinkedList(); 
        for (int i=15; i>0; --i) 
        { 
            llist.push(i); 
            llist.printList(); 
            llist.printMiddle(); 
        } 
    } 
} 