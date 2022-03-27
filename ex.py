
def solution(linked_list):
    slow_pointer = linked_list.head()
    fast_pointer = slow_pointer

    while slow_pointer:
        if slow_pointer.next is None:
            return False

        if fast_pointer.next is None:
            return False

        fast_pointer = fast_pointer.next.next
        if fast_pointer == slow_pointer:
            return True
        slow_pointer = slow_pointer.next
    return False
