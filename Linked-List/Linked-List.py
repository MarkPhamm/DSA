class ListNode:
    def __init__(self, val = None, next = None) -> None:
        # Initialize the value and the next pointer of the ListNode
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        # Initialize head (which is the beginning ListNode)
        self.head = None 

    # Method to insert value at the beginning
    def insert_at_begin(self, data):
        # Create a new ListNode and set it as the head
        self.head = ListNode(data, self.head)
    
    # Method to insert value at the end
    def insert_at_end(self, data):
        # Check if the Linked List is empty
        if self.head is None:
            # Insert at the beginning if the list is empty
            self.insert_at_begin(data)
            return 
        
        # Initiate current node at the head node
        cur = self.head 
        
        # Traverse through to the end node
        while cur.next:
            cur = cur.next 
        
        # Add new node to the end of the list
        cur.next = ListNode(data, None)
    
    def insert_multiple_values(self, data_list):
        # Initialize the head to None before inserting values
        self.head = None
        # Insert each value from the data_list into the LinkedList
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        # Initialize current node and count
        cur = self.head 
        count = 0
        # Traverse through the list to count the nodes
        while cur:
            count += 1
            cur = cur.next
        # Return the total count of nodes
        return count

    def insert_at(self, data, index):
        # Check for valid index
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        # Insert at the beginning if index is 0
        if index == 0:
            self.insert_at_begin(data)
            return
        
        # Initialize count and current node
        count = 0
        cur = self.head
        # Traverse to the position before the desired index
        while cur:
            if count == index - 1:
                # Insert the new ListNode at the specified index
                cur.next = ListNode(data, cur.next)
                break
            cur = cur.next
            count += 1 

    def remove_at(self, index):
        # Check for valid index
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        # Remove the head if index is 0
        if index == 0:
            self.head = self.head.next
            return 

        # Initialize count and current node
        count = 0
        cur = self.head
        # Traverse to the position before the desired index
        while cur:
            if count == index - 1:
                # Remove the node at the specified index
                cur.next = cur.next.next
                break
            cur = cur.next
            count += 1 

    def replace_at(self, data, index):
        # Check for valid index
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        # Replace the head value if index is 0
        if index == 0:
            cur = self.head
            self.head = ListNode(data, cur.next)
            return
        
        # Initialize count and current node
        count = 0
        cur = self.head
        # Traverse to the position before the desired index
        while cur:
            if count == index - 1:
                # Replace the node value at the specified index
                cur.next = ListNode(data, cur.next.next)
                break 
            cur = cur.next
            count += 1

    def print(self):
        # Check if the Linked List is empty
        if self.head is None:
            print("Your Linked List is empty")
            return

        # Initialize string to hold the list representation
        listr = ''
        cur = self.head
        # Traverse through the list to build the string representation
        while cur:
            listr += str(cur.val) + '-->'
            cur = cur.next
        
        # Print the string representation of the Linked List
        print(listr)

def main():
    # Create a new LinkedList instance
    ll = LinkedList()
    # Insert values into the LinkedList
    ll.insert_at_end(5)
    ll.insert_at_begin(1)
    ll.insert_at_end(6)
    
    print(ll.get_length())
    ll.replace_at(2,2)
    ll.print()

    ll.remove_at(2)
    ll.print()
    
if __name__ == "__main__":
    main()
