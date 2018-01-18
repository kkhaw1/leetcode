# -*- coding: utf-8; -*-

"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '%s | %s' % (self.val, ('-> \n %s' % self.next) if self.next else '/')


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sum_list = None
        prev = None

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_over = 0
        curr_l1 = l1
        curr_l2 = l2
        while curr_l1 or curr_l2:
            l1_value = 0
            l2_value = 0

            if curr_l1:
                l1_value = curr_l1.val
                curr_l1 = curr_l1.next
            if curr_l2:
                l2_value = curr_l2.val
                curr_l2 = curr_l2.next
            sum = l1_value + l2_value + carry_over
            new_node_value = sum % 10
            carry_over = sum / 10

            node = ListNode(new_node_value)
            if not prev:
                sum_list = node
                prev = node
            else:
                prev.next = node
                prev = node
        if carry_over:
            prev.next = ListNode(carry_over)

        return sum_list


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(8)
    expected = ListNode(9)
    solution = Solution()
    actual = solution.addTwoNumbers(l1, l2)
    print('%s' % expected)
    print('%s' % actual)

    l1 = ListNode(2)
    l2 = ListNode(8)
    expected = ListNode(0)
    expected.next = ListNode(1)
    solution = Solution()
    actual = solution.addTwoNumbers(l1, l2)
    print('%s' % expected)
    print('%s' % actual)
