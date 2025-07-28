class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    # TODO: implement
    if head.next is None:
        return True
    elif head.next.next is None:
        # only 2 elements in the list
        return head.val == head.next.val
    list_length = 0
    middle_node = None
    slow_pointer = head
    fast_pointer = head
    while fast_pointer:
        if fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            list_length += 2
        else:
            fast_pointer = None
            list_length += 1
            middle_node = slow_pointer
        if fast_pointer:
            slow_pointer = slow_pointer.next
        else:
            middle_node = slow_pointer
    # check numbers are equal from middle point
    # if length is an odd number then do not use middle
    # value for comparison
    if list_length % 2 == 0:
        if middle_node.val != middle_node.next.val:
            return False
    # reverse right posrtion
    right_head = middle_node.next
    left_node = head
    right_node = reverse_linked_list(right_head)
    while right_node is not None:
        if left_node.val != right_node.val:
            return False
        left_node = left_node.next
        right_node = right_node.next
    return True

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def swap_linked_list_nodes(head, start, end):
    # TODO: implement
    if start == end or head.next is None:
        return head
    index = 0
    start_node = None
    end_node = None
    current_node = head
    start_previous = None
    end_previous = None
    previous_node = None
    while current_node:
        if index == start:
            start_node = current_node
            start_previous = previous_node
        elif index == end:
            end_node = current_node
            end_previous = previous_node
            break
        previous_node = current_node
        current_node = current_node.next
        index += 1
    if start_node and end_node:
        end_previous.next = start_node
        if start_previous:
            start_previous.next = end_node
        else:
            head = end_node
        temp_pointer = end_node.next
        end_node.next = start_node.next
        start_node.next = temp_pointer
        return head
    else:
        return None

def remove_duplicates(head):
    # TODO: implement the solution in O(n) complexity
    all_numbers = set()
    current_node = head
    previous_node = head
    while current_node:
        if current_node.val in all_numbers:
            remove_link(previous_node, current_node)
            current_node = previous_node.next
        else:
            all_numbers.add(current_node.val)
            previous_node = current_node
            current_node = current_node.next
    return head

def remove_link(remaining_node, deleting_node):
    remaining_node.next = deleting_node.next
    deleting_node.next = None

def rotate_right(head: ListNode, k: int) -> ListNode:
    # TODO: Implement the solution here.
    if head.next is None or k == 0:
        return head
    list_length = 1
    current_node = head
    while current_node.next:
        list_length += 1
        current_node = current_node.next
    end_node = current_node
    k = k % list_length
    if k == 0:
        return head
    end_node.next = head
    position = list_length - k - 1
    new_end_node = head
    for _ in range(position):
        new_end_node = new_end_node.next
    new_head = new_end_node.next
    new_end_node.next = None
    return new_head

def hasCycle(head):
    # TODO: implement cycle detection in the linked list
    if head.next is None:
        return False
    slow_pointer = head
    fast_pointer = head
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            return True
    return False

if __name__ == "__main__":
    # head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
    # head = swap_linked_list_nodes(head, 1, 2)
    # head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    # head = rotate_right(head, 1)
    # head = ListNode(0, ListNode(1))
    # head = rotate_right(head, 1)
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(2))))
    # print(swap_linked_list_nodes(head, 1, 3))
    head2 = ListNode(1, ListNode(2, ListNode(3)))
    print(hasCycle((head2)))
    nodes = [ListNode(i) for i in range(1, 100001)]
    for i in range(100000):
        nodes[i].next = nodes[(i + 1) % 100000]
    head6 = nodes[0]
    print(hasCycle((head6)))