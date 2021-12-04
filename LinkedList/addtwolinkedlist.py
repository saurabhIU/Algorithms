import LinkedList

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    output = output_head = None
    carry = 0
    while linkedListOne is not None or linkedListTwo is not None or carry != 0:
        val1 = linkedListOne.value if linkedListOne is not None else 0
        val2 = linkedListTwo.value if linkedListTwo is not None else 0
        sum = val1 + val2 + carry
        new_sum = sum % 10
        if output is None:
            output = LinkedList(new_sum)
            output_head = output
        else:
            output.next = LinkedList(new_sum)
            output = output.next
        carry = sum // 10
        linkedListOne = linkedListOne.next if linkedListOne is not None else None
        linkedListTwo = linkedListTwo.next if linkedListTwo is not None else None

    return output_head


def findLoop(head):
    # Write your code here.
    slow = fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow.value == fast.value:
            loop_ptr = head
            while loop_ptr and slow:
                if loop_ptr.value == slow.value:
                    return loop_ptr
                else:
                    loop_ptr = loop_ptr.next
                    slow = slow.next
    return False

def reverselinkedlist(head):

    current = head
    previous = None

    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous

def mergeLinkedLists(headOne, headTwo):

    one = headOne
    two = headTwo
    previous = None

    while one is not None and two is not None:
        if one.value < two.value:
            previous  = one
            one = one.next
        else:
            if previous is not None:
                previous.next = two
            previous = two
            two = two.next
            previous.next = one

    if two is not None:
        previous.next = two
    return headOne if headOne.value < headTwo.value else headTwo



ll1 = LinkedList(9).addMany([9, 9])
ll2 = LinkedList(9).addMany([9, 9,9,9])
ll1 = LinkedList(9)
ll2 = LinkedList(2)
actual = sumOfLinkedLists(ll1, ll2)
print(LinkedList.getNodesInArray(actual))
# print(LinkedList.getNodesInArray(expected))
test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
# test.getNthNode(10).next = test.getNthNode(5)
# x = findLoop(test)
# print(LinkedList.getNodesInArray(x))

print(f"Original linked list is {LinkedList.getNodesInArray(test)}")

reversed = reverselinkedlist(test)
print(f"Reversed linked list is {LinkedList.getNodesInArray(reversed)}")

list1 = LinkedList(2).addMany([6, 7, 8])
list2 = LinkedList(1).addMany([3, 4, 5, 9, 10])
mergedList = mergeLinkedLists(list1,list2)
print(f"Reversed linked list is {LinkedList.getNodesInArray(mergedList)}")