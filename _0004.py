# -*- coding: utf-8; -*-

import sys

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

"""
ensure nums1 is the shorter array
total_length = (len(nums1) + len(nums)2)
desired_length_left_side = (total_length if total_length%2 == 0 else total_length + 1)/2
desired_length_right_side = total_length - desired_length_left_side

x = len(nums1)
y = len(nums2)

partition the arrays and do comparison:
    if left_nums1 <= right_nums2
        left_nums2 <= right_nums1:
        - Found partition
        - total_length is even:
            median = avg(max(left_nums1, left_nums2), min(right_nums1, right_nums2))
        else
            median = max(left_nums1, left_nums2)
    else if left_nums1 > right_nums2:
        move nums1 partition to the left
    else if left_nums2 > right_nums1:
        move nums1 partition to the right


n1 [ 1, 5, 7, 15, 22]
n2 [ 2, 6, 17, 25, 42]
m = [ 1, 2, 5, 6, 7, 15, 17, 22, 25, 42 ] = 7+15 / 2 = 11

x = 5
y = 5
desired_left_len = 5

low     0
high    5
p_x     2
p_y     3
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)

        median = 0

        x, y = len(nums1), len(nums2)
        total_length = x + y

        low, high = 0, x
        while low <= high:
            partition_x = (high + low) / 2
            partition_y = ((total_length + 1) / 2) - partition_x

            left_x = (-sys.maxint - 1) if partition_x == 0 else nums1[partition_x - 1]
            right_x = sys.maxint if partition_x == x else nums1[partition_x]

            left_y = (-sys.maxint - 1) if partition_y == 0 else nums2[partition_y - 1]
            right_y = sys.maxint if partition_y == y else nums2[partition_y]

            if left_x <= right_y and left_y <= right_x:
                if total_length % 2 == 0:
                    median = (max(left_x, left_y) + min(right_x, right_y)) / 2.0
                else:
                    median = max(left_x, left_y)
                break
            elif left_x > right_y:
                high = partition_x - 1
            else:
                low = partition_x + 1

        return median


if __name__ == '__main__':
    test_cases = [
        {
            'l1': [1],
            'l2': [3],
            'median': 2,
        },
        {
            'l1': [1, 2, 3, 4, 5],
            'l2': [6, 7, 8, 9, 10],
            'median': 5.5,
        },
        {
            'l1': [1, 3],
            'l2': [2],
            'median': 2,
        },
        {
            'l1': [1, 2],
            'l2': [3, 4],
            'median': 2.5,
        },
        {
            'l1': [2, 4, 6, 8],
            'l2': [102, 104, 106, 108, 110, 112],
            'median': 103,
        },
    ]
    solution = Solution()
    for test_case in test_cases:
        actual = solution.findMedianSortedArrays(test_case['l1'], test_case['l2'])
        try:
            assert test_case['median'] == actual
            print "Test case passed: l1=%s l2=%s, median:%s" % (test_case['l1'], test_case['l2'], test_case['median'])
        except AssertionError as e:
            print('Failed to assert that:\n  Expected: %s\n  Actual:   %s\n[%s] [%s]' % (test_case['median'], actual, test_case['l1'], test_case['l2']))

