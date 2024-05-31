class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy
    
    l1, l2 = list1, list2
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # If one of the lists is not empty, append it
    if l1:
        current.next = l1
    else:
        current.next = l2
    
    return dummy.next

# Example usage:
# Creating list1: 1 -> 2 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))
# Creating list2: 1 -> 3 -> 4
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Merging lists
merged_list = mergeTwoLists(list1, list2)

# Function to print the linked list
def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next

printList(merged_list)
