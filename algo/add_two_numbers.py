class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def bf_add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    result_list = ListNode(0)
    current = result_list
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        total = x + y + carry

        carry = total // 10
        current.next = ListNode(total % 10)

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

        current = current.next

    if carry > 0:
        current.next = ListNode(carry)

    return result_list.next


def add_two_numbers(li1: ListNode, li2: ListNode) -> ListNode:
    return bf_add_two_numbers(li1, li2)


if __name__ == '__main__':
    list1 = ListNode(2, ListNode(4, ListNode(3)))
    list2 = ListNode(5, ListNode(6, ListNode(4)))
    print(add_two_numbers(list1, list2))
