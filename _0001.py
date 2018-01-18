# -*- coding: utf-8; -*-

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        sums_list = {}
        for key, value in enumerate(nums):
            compliment = target - value
            if compliment in sums_list:
                return [sums_list[compliment], key]
            sums_list[value] = key

        raise Exception('Sum pair not found')


if __name__ == '__main__':
    tests = [
        {
            "nums": [2, 7, 11, 15],
            "target": 9,
            "expected": [0, 1],
        },
        {
            "nums": [1, 3, 7, 10],
            "target": 11,
            "expected": [0, 3],
        },
        {
            "nums": [1, 5, 15, 25, 30, 100],
            "target": 35,
            "expected": [1, 4],
        },
        {
            "nums": [3, 2, 4],
            "target": 6,
            "expected": [1, 2],
        }
    ]
    for test_case in tests:
        solution = Solution()
        actual = solution.twoSum(test_case['nums'], test_case['target'])
        try:
            assert test_case['expected'] == actual
            print "Test case passed: nums=%s target=%s" % (test_case['nums'], test_case['target'])
        except AssertionError as e:
            print('Failed to assert that:\n  Expected: %s\n  Actual:   %s\n' % (test_case['expected'], actual))
