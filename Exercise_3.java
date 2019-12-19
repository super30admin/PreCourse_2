Time Complexity-O(n/2)=O(n)
Space Complexity-O(1)
package com.company;

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
    void printMiddle() {
        if (head != null) {
            Node fast = head;
            Node slow = head;
            while (fast != null && fast.next != null) {
                slow = slow.next;
                fast = fast.next.next;
            }
            System.out.println("Middle element is: " + slow.data);
        }
    }

    public void push(int new_data)
    {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }

    public void printList()
    {
        if(head!=null) {
            Node tnode = head;
            while (tnode != null) {
                System.out.print(tnode.data + "->");
                tnode = tnode.next;
            }
            System.out.println("NULL");
        }
    }

    public static void main(String [] args)
    {
        LinkedList llist = new LinkedList();
        for (int i=5; i>0; --i)
        {
            llist.push(i);
            llist.printList();
            llist.printMiddle();
        }
    }
}
