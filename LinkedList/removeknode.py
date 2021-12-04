# Remove K'th node from end of a Linked list

import LinkedList

def removeKthNodeFromEnd(self, head, k):
    first_node = second_node = head
    parent_node = None
    for i in range(k):
        first_node = first_node.next
    while first_node:
        parent_node = second_node
        second_node = second_node.next

        first_node = first_node.next
    if parent_node:
        parent_node.next = second_node.next
        second_node.next = None
    else:
        head.value = head.next.value
        head.next = head.next.next
    return head


linkedListClass = LinkedList(0)
linkedListClass.addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
linkedListClass.removeKthNodeFromEnd(linkedListClass, 10)
print(linkedListClass.getNodesInArray())
