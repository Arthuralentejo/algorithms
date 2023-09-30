import unittest

from algo.add_two_numbers import add_two_numbers, ListNode


def list_to_array(head: ListNode) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class TestAddTwoNumbers(unittest.TestCase):
    def test_example_1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        result = add_two_numbers(l1, l2)
        expected_result = ListNode(7, ListNode(0, ListNode(8)))
        self.assertEqual(list_to_array(result), list_to_array(expected_result))

    def test_example_2(self):
        l1 = ListNode(0)
        l2 = ListNode(0)
        result = add_two_numbers(l1, l2)
        expected_result = ListNode(0)
        self.assertEqual(list_to_array(result), list_to_array(expected_result))

    def test_example_3(self):
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        result = add_two_numbers(l1, l2)
        expected_result = ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(
            1))))))))
        self.assertEqual(list_to_array(result), list_to_array(expected_result))


if __name__ == '__main__':
    unittest.main()
