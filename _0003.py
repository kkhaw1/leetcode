# -*- coding: utf-8; -*-

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        max_end = 0
        max_start = 0

        start = 0
        end = 0
        length_s = len(s)
        visited = {}
        while 0 <= start <= end <= length_s:
            if start == 0 and end == 0:
                visited[s[end]] = end

            if end + 1 >= length_s:
                break
            elif end + 1 <= length_s and s[end + 1] not in visited:
                end += 1
                visited[s[end]] = end
                if (end - start) > (max_end - max_start):
                    max_start = start
                    max_end = end
            else:
                if start != end:
                    del visited[s[start]]
                end = end + 1 if start == end else end
                start += 1

        return max_end - max_start + 1


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        {
            'str': 'abcabcbb',
            'expected': 'abc',
        },
        {
            'str': 'bbbbb',
            'expected': 'b',
        },
        {
            'str': 'pwwkew',
            'expected': 'wke',
        },
        {
            'str': 'abcdefghijklmnop',
            'expected': 'abcdefghijklmnop',
        },
        {
            'str': 'dvdf',
            'expected': 'vdf',
        },
        {
            'str': '',
            'expected': '',
        },
    ]

    for test_case in test_cases:
        actual = solution.lengthOfLongestSubstring(test_case['str'])
        try:
            assert len(test_case['expected']) == actual
            print "Test case passed: str=%s substring=%s" % (test_case['str'], test_case['expected'])
        except AssertionError as e:
            print('Failed to assert that:\n  Expected: %s\n  Actual:   %s\n' % (test_case['expected'], actual))
