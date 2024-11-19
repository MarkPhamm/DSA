class ListNode():
    def __init__(self, val = None, next = None) -> None:
        self.val = val
        self.next = next
    
class LinkedList():
    # Initialize the Linked List
    def __init__(self) -> None:
        self.head = None 
        self.size = 0
    
    # Operations:
    # addFirst(Node newNode): Adds a node to the beginning of the list in O(1) time.
    def addFirst(self, val: int) -> None:
        self.head = ListNode(val, self.head)
        self.size +=1
    
    # addLast(Node newNode): Adds a node to the end of the list in O(1) time.
    # (Hint: Keep track of the last node.)
    def addLast(self, val: int) -> None: 
        if self.head is None: 
            self.addFirst(val)
        else:
            dummy = ListNode()
            dummy.next = self.head
            cur = dummy

            while cur.next:
                cur = cur.next 
            
            cur.next = ListNode(val, None)
            
            self.size +=1

    
    # search(int val): Searches for a node with the specified value in O(n) time.
    def search(self, val: int) -> None:
        pass

    # remove(int val): Removes the first node with the specified value in O(n) time.
    #   (If multiple nodes have the same value, remove the first one found.)
    def remove(self, val: int) -> None:
        dummy = ListNode()
        dummy.next = self.head
        cur = dummy.next 
        prev = dummy 

        while cur:
            if cur.val == val:
                prev.next = prev.next.next 
            cur = cur.next
            prev = prev.next
        

    # getSize(): Returns the size of the linked list in O(1) time.
    def getSize(self):
        return self.size
    
    # removeFirst(): Removes the first node in O(1) time.
    def removeFirst(self):
        dummy = ListNode()
        dummy.next = self.head
        cur = dummy 

        self.head = cur.next.next
        
        self.size -=1
    
    # removeLast(): Removes the last node in O(1) time.
    def removeLast(self):
        dummy = ListNode()
        dummy.next = self.head
        cur = dummy 
        
        count = 0
        size = self.getSize()

        while cur.next:
            if count == size - 1:
                cur.next = None
                break
            count += 1
            cur = cur.next

        self.size -=1

    # removeAll(): remove all the elements in O(n)
    
    # print(): print the linked list
    def print(self):
        cur = self.head 

        strl = ""
        while cur:
            strl += (str(cur.val) + "-->")
            cur = cur.next
        strl += "None"
        print(strl)
        

def main():    
    # Test addFirst
    submit = True
    
    if submit:
        ll = LinkedList()
        ll.addFirst(4)
        ll.addLast(5)
        ll.addLast(6)
        ll.addLast(7)
        ll.removeLast()
        ll.removeFirst()
        ll.print()
        print(ll.getSize())
        # Test Cases
        print("Running Test Cases...")
        ll.addFirst(10)
        assert ll.getSize() == 3, "Test Case 1 Failed"
        ll.print()  # Expected: 10-->5-->6-->None

        # Test addLast
        ll.addLast(20)
        assert ll.getSize() == 4, "Test Case 2 Failed"
        ll.print()  # Expected: 10-->5-->6-->20-->None

        # Test removeFirst
        ll.removeFirst()
        assert ll.getSize() == 3, "Test Case 3 Failed"
        ll.print()  # Expected: 5-->6-->20-->None

        # Test removeLast
        ll.removeLast()
        assert ll.getSize() == 2, "Test Case 4 Failed"
        ll.print()  # Expected: 5-->6-->None

        print("All test cases passed!")

if __name__ == "__main__":
    main()