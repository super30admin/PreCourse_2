package PreCourses2;

/*
Time Complexity:
    Best Case: O(n)
    Average Case: O(n)
    Worst Case: O(n)
Space Complexity:
    O(n)
 */

public class linklistMiddleElemnt {
    private static Node head;
    static class Node {
        int data;
        Node next;
        Node(int data) {
            this.data = data;
            next = null;
        }
    }

    private void printMiddle() {
        Node slow = head;
        Node fast = head;
        Node temp = head;
        if(temp != null) {
            while(fast != null && fast.next != null) {
                slow = slow.next;
                fast = fast.next.next;
            }
        }
        System.err.println("Middle element of the Linked List will be: " + slow.data);
    }

    private void push(int new_data)
    {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }

    public void printList()
    {
        Node temp = head;
        while (temp != null)
        {
            System.out.print(temp.data + "->");
            temp = temp.next;
        }
        System.out.println("NULL");
    }

    public static void main(String[] args) {
        linklistMiddleElemnt llist = new linklistMiddleElemnt();
        for(int i = 15; i > 0; i--)
        {
            llist.push(i);
        }
        llist.printList();
        llist.printMiddle();
    }
}