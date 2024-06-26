class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Example usage:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original linked list:")
print_linked_list(head)

reversed_head = reverse_linked_list(head)

print("Reversed linked list:")
print_linked_list(reversed_head)
